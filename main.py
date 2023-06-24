import urllib.request
import json

def get_latest_stories():
    url = "https://time.com"
    response = urllib.request.urlopen(url)
    html_content = response.read().decode('utf-8')

    # Find the start and end markers for the latest stories section
    start_marker = '<section class="latest">'
    end_marker = '</section>'
    start_index = html_content.find(start_marker)
    end_index = html_content.find(end_marker, start_index)

    if start_index != -1 and end_index != -1:
        latest_stories_html = html_content[start_index:end_index]
        stories = []

        # Find the title and link for each story
        title_marker = '<h2>'
        link_marker = '<a href="'
        while title_marker in latest_stories_html and link_marker in latest_stories_html:
            title_start = latest_stories_html.find(title_marker)
            title_end = latest_stories_html.find('</h2>', title_start)
            title = latest_stories_html[title_start+len(title_marker):title_end].strip()

            link_start = latest_stories_html.find(link_marker)
            link_end = latest_stories_html.find('"', link_start+len(link_marker))
            link = latest_stories_html[link_start+len(link_marker):link_end]

            stories.append({
                'title': title,
                'link': url + link
            })

            latest_stories_html = latest_stories_html[link_end:]

        return stories[:6]

    return None

# Call the function to get the latest stories
stories = get_latest_stories()

# Print the stories
if stories:
    json_stories = json.dumps(stories, indent=4)
    print(json_stories)
#else:
 # print("Failed to find the latest stories section in the HTML.")
