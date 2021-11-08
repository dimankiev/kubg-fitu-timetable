from lxml import html
import requests

def rec_link_look(links, text):
    for link in links:
        if isinstance(link, list):
            return rec_link_look(link, text)
        elif text in link.text_content().strip():
            return link
        else:
            continue

def rec_lists_filter(lists, text):
    for accordionlist in lists:
        if isinstance(accordionlist, list):
            return rec_lists_filter(accordionlist, text)
        
        title = accordionlist.xpath('./parent::div/parent::div/div[@class="accordion-heading panel-heading"]/a/span')
        
        if text in title[0].text_content().strip():
            return accordionlist
        else:
            continue

def get_timetable_url():
    linkto_main_page = 'https://fitu.kubg.edu.ua'

    page = requests.get(linkto_main_page)
    code = html.fromstring(page.content)

    all_links = code.xpath('//a')

    looking_for = 'Денна форма навчання'
    our_link = rec_link_look(all_links, looking_for)

    page = requests.get(linkto_main_page + our_link.get('href'))
    code = html.fromstring(page.content)

    all_lists = code.xpath('//div[@class="accordion-inner panel-body"]')

    discipline = 'Кібербезпека'
    filtered = rec_lists_filter(all_lists[::-1], discipline)

    course = '3'

    timetable_url = 'not found'

    for link in filtered.xpath('./p/a'):
        text = link.xpath('./span/text()')[0].strip()
        if ('%s курс' % course) in text:
            timetable_url = link.get('href')
            break

    return linkto_main_page + timetable_url
