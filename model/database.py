from model.connection_pool import get_connection

#this model is used to operate AWS RDS database

# save data to AWS RDS MySQL database
def save_data(content: str, file_name: str):
    connection = None
    cursor = None
    try:
        image_url = f"https://drvdlpgjj97z5.cloudfront.net/{file_name}" # CloudFront URL
        connection = get_connection()
        cursor = connection.cursor()
        sql = "INSERT INTO message (content, image_url) VALUES (%s, %s)"
        values = (content, image_url)
        cursor.execute(sql, values)
        connection.commit()  
        
        if cursor.rowcount == 1:  # check execute cursor scope
            response = {
                "success": True,
                "id": cursor.lastrowid,  # Get the ID of the last inserted record
                "content": content,
                "img_url": image_url
            }
        else:
            response = {
                "success": False,
                "message": "Insert operation did not affect any rows"
            }
        return response    
    except Exception as e:
        raise ValueError(f"Error while inserting to MySQL: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

#get all message data from AWS RDS MySQL database
def get_data():
    connection = None
    cursor = None
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.excute(
            "SELECT * FROM message"
        )
        result = cursor.fetchall()
    except Exception as e:
        raise ValueError(f"Error while searching message data: {e}") 
    try:
        formatted_result = []
        for row in result:
            formatted_row = {
                "id":row[0],
                "content":row[1],
                "image_url":row[2],
                "create_at":row[3]
            }
            formatted_result.append(formatted_row)
        return formatted_result
    except Exception as e:
        raise ValueError(f"Error while formatted message data: {e}") 