from bs4 import BeautifulSoup
from requests import get


def extract_wwr_jobs(keyword):
  base_url = "https://weworkremotely.com/categories/"
  response = get(f"{base_url}{keyword}")
  if response.status_code != 200:
    print("웹사이트를 찾을수 없습니다.")
  else:
    results = []
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all('section', class_="jobs")
    for job_section in jobs:
      job_post = job_section.find_all('li', class_="feature")
      for post in job_post:
        anchors = post.find_all('a')
        anchor = anchors[1]
        link = anchor["href"]
        company, kind, location = anchor.find_all('span', class_="company")
        title = anchor.find('span', class_='title')
        job_data = {
            'link': f"https://weworkremotely.com{link}",
            'company': company.string,
            'location': location.string,
            'position': title.string
        }
        results.append(job_data)
    return results