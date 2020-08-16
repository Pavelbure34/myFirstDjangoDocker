import graphene
from graphene_django import DjangoObjectType
from myfirstdjango.article.models import Article
from myfirstdjango.reply.models import Reply

class ArticleType(DjangoObjectType):
    class Meta:
        model = Article
        fields = (
            "unique_id",
            "end_point",
            "title",
            "author",
            "posted_DateTime",
            "likes",
            "contents",
            "replies"
        )

class ReplyType(DjangoObjectType):
    class Meta:
        model = Reply
        fields = (
            "unique_id",
            "author",
            "posted_DateTime",
            "contents",
            "target_article"
        )

class Query(graphene.ObjectType):
    all_articles = graphene.List(ArticleType)
    all_replies = graphene.List(ReplyType)
    category_by_article = graphene.Field(ArticleType, unique_id=graphene.String(required=True))
    category_by_reply = graphene.Field(ReplyType, unique_id=graphene.String(required=True))

    def resolve_all_articles(root, info):
        # We can easily optimize query count in the resolve method
        return Article.objects.select_related("article").all()
    def resolve_all_replies(root, info):
        # We can easily optimize query count in the resolve method
        return Reply.objects.select_related("reply").all()

    def resolve_category_by_article(root, info, title):
        try:
            return Article.objects.get(title=title)
        except Article.DoesNotExist:
            return None

    def resolve_category_by_reply(root, info, author):
        try:
            return Reply.objects.get(author=author)
        except Reply.DoesNotExist:
            return None

schema = graphene.Schema(query=Query)
