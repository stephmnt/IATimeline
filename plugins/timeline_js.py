from pelican import signals
import os
import json

def articles_to_timeline(generator):
    timeline_media_url = generator.settings.get('TIMELINE_MEDIA_URL', '/theme/images/overlay.png')
    timeline_caption = generator.settings.get('TIMELINE_CAPTION', 'Default Caption')
    timeline_credit = generator.settings.get('TIMELINE_CREDIT', 'Photo by Example')
    timeline_headline = generator.settings.get('TIMELINE_HEADLINE', 'Default Headline')
    timeline_text = generator.settings.get('TIMELINE_TEXT', '<p>Default description text.</p>')

    events = []
    for article in generator.articles:
        # Create start_date dictionary
        start_date = {
            'year': article.metadata.get('year', ''),
            'month': article.metadata.get('month', ''),
            'day': article.metadata.get('day', ''),
            'hour': article.metadata.get('hour', ''),
            'minute': article.metadata.get('minute', ''),
            'second': article.metadata.get('second', ''),
            'millisecond': article.metadata.get('millisecond', ''),
            'display_date': article.metadata.get('display_date', '')
        }

        # Create end_date dictionary only if there's relevant data
        end_date = {
            'year': article.metadata.get('end_year', ''),
            'month': article.metadata.get('end_month', ''),
            'day': article.metadata.get('end_day', ''),
            'hour': article.metadata.get('end_hour', ''),
            'minute': article.metadata.get('end_minute', ''),
            'second': article.metadata.get('end_second', ''),
            'millisecond': article.metadata.get('end_millisecond', ''),
            'display_date': article.metadata.get('end_display_date', '')
        }

        # Filter out empty values and only add end_date if it's not empty
        end_date = {k: v for k, v in end_date.items() if v}
        event = {
            'start_date': start_date,
            'text': {
                'headline': article.metadata.get('headline', article.title),
                'text': article.metadata.get('text', '') # variante intéressante : article.content
            },
            'media': {
                'url': article.metadata.get('media', ''),
                'caption': article.metadata.get('caption', ''),
                'thumbnail': article.metadata.get('thumbnail', ''),
                'alt': article.metadata.get('alt', ''),
                'title': article.metadata.get('media_title', ''),
                'link': article.metadata.get('link', ''),
                'target': article.metadata.get('target', '')
            },
            'background': article.metadata.get('background', ''),
            'group': article.metadata.get('group', ''),
            'autolink': article.metadata.get('autolink', ''),
            'type': article.metadata.get('type', '')
        }
        if end_date:  # Only add end_date if it contains any data
            event['end_date'] = end_date

        events.append(event)

    timeline_data = {
        'title': {
            'media': {
                'url': timeline_media_url,
                'caption': timeline_caption,
                'credit': timeline_credit
            },
            'text': {
                'headline': timeline_headline,
                'text': timeline_text
            }
        },
        'events': events
    }

    with open(os.path.join(generator.output_path, 'timeline.json'), 'w') as f:
        json.dump(timeline_data, f, indent=4)

def register():
    signals.article_generator_finalized.connect(articles_to_timeline)
