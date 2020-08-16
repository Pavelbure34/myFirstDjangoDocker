### Models to be used in this App

1. article
    - create
        - unique_id: unique id
        - end_point(url)
        - title
        - author
        - posted_DateTime
        - likes
        - contents
        - replies
    - delete
        - id: unique id

2. reply
    - create
        - unique_id: unique id
        - target_article
        - author
        - posted_DateTime
        - contents
    - delete
        - id : unique id

