import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('Books')

with table.batch_writer() as batch:
    batch.put_item(Item={"Author": "John Grisham", "Title": "The Rainmaker",
        "Category": "Suspense", "Formats": { "Hardcover": "J4SUKVGU", "Paperback": "D7YF4FCX" } })
    batch.put_item(Item={"Author": "John Grisham", "Title": "The Firm",
        "Category": "Suspense", "Formats": { "Hardcover": "Q7QWE3U2",
        "Paperback": "ZVZAYY4F", "Audiobook": "DJ9KS9NM" } })
    batch.put_item(Item={"Author": "James Patterson", "Title": "Along Came a Spider",
        "Category": "Suspense", "Formats": { "Hardcover": "C9NR6RJ7",
        "Paperback": "37JVGDZG", "Audiobook": "6348WX3U" } })
    batch.put_item(Item={"Author": "Dr. Seuss", "Title": "Green Eggs and Ham",
        "Category": "Children", "Formats": { "Hardcover": "GVJZQ7JK",
        "Paperback": "A4TFUR98", "Audiobook": "XWMGHW96" } })
    batch.put_item(Item={"Author": "William Shakespeare", "Title": "Hamlet",
        "Category": "Drama", "Formats": { "Hardcover": "GVJZQ7JK",
        "Paperback": "A4TFUR98", "Audiobook": "XWMGHW96" } })
