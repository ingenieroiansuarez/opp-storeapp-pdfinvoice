import pandas

df = pandas.read_csv("articles.csv", dtype={"id": str})

class Article:
    def __init__(self, article_id):
        self.article_id = article_id
        self.name = df.loc[df["id"] == self.article_id, "name"].squeeze()
        self.price = df.loc[df["id"] == self.article_id, "price"].squeeze()

    def purchase(self):
        """Purchase an article by changing its availability to no."""
        df.loc[df["id"] == self.article_id, "available"] = "no"
        df.to_csv("articles.csv", index=False)

    def available(self):
        '''Check if the article is available for purchase.'''
        availability = df.loc[df["id"] == self.article_id, "available"].squeeze()
        return availability == "yes"

class Receipt:
    def __init__(self, customer_name, article_object):
        self.customer_name = customer_name
        self.article = article_object

    def generate(self):
        content = f'''
        Receipt, thank you for your purchase!
        Customer Name: {self.customer_name}
        Article Name: {self.article.name}
        Price: {self.article.price}
        '''
        return content

print(df)
article_ID = input("Enter article id: ")
article = Article(article_ID)
if article.available():
    article.purchase()
    name = input("Enter your name: ")
    receipt = Receipt(customer_name=name, article_object=article)
    print(receipt.generate())
    print("Article is available")
else:
    print("Article is not available")
# Note: Ensure that the articles.csv file exists and has the appropriate structure.