from model.connection_pool import get_connection


# save data to MySQL database
def save_message(content: str, file_name: str):
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
            