#!/usr/bin/env python3

from datetime import datetime
from x8.models import Article

def test_article_creation():
    try:
        # Test creating Article with created_at
        article = Article(
            unique_id='test-123',
            url='https://example.com',
            title='Test Article',
            keywords='test,python',
            description='A test article',
            text_content='This is the content',
            src='test_source',
            published_date=datetime.now(),
            content_url='https://example.com/content',
            created_at=datetime.now()
        )
        print(f"SUCCESS: Article created with unique_id: {article.unique_id}")
        print(f"Created at: {article.created_at}")
        return True
    except Exception as e:
        print(f"ERROR: {e}")
        return False

if __name__ == "__main__":
    test_article_creation()
