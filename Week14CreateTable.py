import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TVShows')

item_1 = {"Network":"TBS", "Title":"Saved By The Bell"}
item_2 = {"Network":"Cartoon Network", "Title":"Tom and Jerry"}
item_3 = {"Network":"HGTV", "Title":"Love It or List It"}
item_4 = {"Network":"HULU", "Title":"Family Matters"}
item_5 = {"Network":"BET", "Title":"Martin"}
item_6 = {"Network":"Nickelodeon", "Title":"Sponge Bob Squarepants"}
item_7 = {"Network":"HBO Max", "Title":"Full House"}
item_8 = {"Network":"TNT", "Title":"House"}
item_9 = {"Network":"BET", "Title":"The Fresh Prince of Bel-Air"}
item_10 = {"Network":"Peacock", "Title":"Monk"}

items_to_add = [item_1, item_2, item_3, item_4, item_5, item_6, item_7, item_8, item_9, item_10]

with table.batch_writer() as batch:
    for item in items_to_add:
        response = batch.put_item(Item={
            "Network": item["Network"],
            "Title": item["Title"]
    }
)

items_to_delete = [item_1, item_2]

with table.batch_writer() as batch:
    for item in items_to_delete:
        response = batch.put_item(Item={
            "Network": item["Network"],
            "Title": item["Title"]
    }
)

print("table")
