# Scrape-Result-pk

Retrieves the scrape result for a specific job.

**URL** : `api/jobs/scrape-result/:pk`

**Method** : `GET`

**Auth required** : AUTHENTICATION

<br>

**Code** : `200 OK`

**Content example**

```json
api/jobs/scrape-result/Data Scientist/

{
    "recommended_jobs": [
        {
            "title": "Data Scientist - 12241483314",
            "matching_skills": [
                "sql",
                "python",
                "r",
                "git"
            ],
            "missing_skills": [
                "basic"
            ],
            "company_name": "Genzeon India4.3",
            "location": "Pune",
            "avg_base_pay_est": "#N/A",
            "company_rating": "4.3",
            "company_link": "https://glassdoor.co.in/partner/jobListing.htm?pos=213&ao=1136043&s=58&guid=00000187c7f8bed18a285e2ce6fd570e&src=GD_JOB_AD&t=SR&vt=w&ea=1&cs=1_d16137f7&cb=1682687180762&jobListingId=1008596704544&jrtk=3-0-1gv3vhfngjfl1801-1gv3vhfo6ghqf800-8f01fe70ccada653-",
            "time_since_posted": "24h",
            "company_skills": [
                "sql",
                "python",
                "r",
                "basic",
                "git"
            ]
        },
        {
            "title": "Senior Consultant | CF- Delta | Analytics | India",
            "matching_skills": [
                "sql",
                "python",
                "r",
                "git"
            ],
            "missing_skills": [
                "Flask",
                "postgresql"
            ],
            "company_name": "FTI Consulting, Inc.4.1",
            "location": "New Delhi",
            "avg_base_pay_est": "₹7,52,328 /yr (est.)",
            "company_rating": "4.1",
            "company_link": "https://glassdoor.co.in/partner/jobListing.htm?pos=109&ao=1110586&s=58&guid=00000187c7f70c3599d26a0e5ccdaef2&src=GD_JOB_AD&t=SR&vt=w&cs=1_4b67fdbc&cb=1682687069517&jobListingId=1008597588245&cpc=F583A5AE0DDDFE3A&jrtk=3-0-1gv3ve333jrqb801-1gv3ve33q21v5000-936ca934915dae3c--6NYlbfkN0Cg7HZUmJnRV4dKO0I4YgUBnE_R5BIjwxrqoegT7KJNQdExlbPfp0S1v9ryyO5s1KD5FQPdOyItOJgP3-0IYApBZzE7RXA9LHLzizJ7dBLwck4DTRnF4QGhTcrx4RLXfK9Y46I2eeK55i0PkdkrmbZerpABxTpoQAK6tRhnpRLNjmtX_5img4TrU7sNxdtqFAsmb8Symc0R0PWVoY4HbDoEGdi7ZQbn_OUqoO6uNZYS9zxEhVaW8U75wFLWD2xTwQVwjuEvROiTtAsUyhhC2VI2RxwT1PwUnKajH_7j0jsnVhrR2GA4KOh7iHuS27AE0HwzRZJmy-J2F3JeixtNTlr-QlVBWSmnN667d5QBpDH94aQOHZ-aNX9slK7Huj9qbBmxsSvMXuW3ocFwRsd4JznxIduD-BPGJzfPQj1XyxNk0gepcyyeP6EVvZW5cZBCQKOw7pyrgjRxX7iEhDcQrrN0nQhTZG3kPYzMML3z4qb8oIH8I-ZWK0GrhUzBXf65QrPIAZi6U-vILY8tk94WpfZnQ1PoX3PcrqbQzV3K4XYqq8CJb3JoeYRYXI_sQXTTE6oe0azjGy9i4kjIKgLkzz0iA9Q-iGPicL3-vjJ68WHpOM9dxyqgQC0b",
            "time_since_posted": "30d+",
            "company_skills": [
                "sql",
                "python",
                "r",
                "Flask",
                "postgresql",
                "git"
            ]
        },
        {
            "title": "Data Scientist",
            "matching_skills": [
                "sql",
                "python",
                "r",
                "git"
            ],
            "missing_skills": [
                "postgresql",
                "mysql",
                "gcp"
            ],
            "company_name": "Dyson3.0",
            "location": "Bangalore",
            "avg_base_pay_est": "#N/A",
            "company_rating": "3.0",
            "company_link": "https://glassdoor.co.in/partner/jobListing.htm?pos=104&ao=1136043&s=58&guid=00000187c7f70c3599d26a0e5ccdaef2&src=GD_JOB_AD&t=SR&vt=w&cs=1_ec3e7c3e&cb=1682687069516&jobListingId=1008613464006&jrtk=3-0-1gv3ve333jrqb801-1gv3ve33q21v5000-01c184c6bd6ea631-",
            "time_since_posted": "30d+",
            "company_skills": [
                "sql",
                "python",
                "r",
                "mysql",
                "postgresql",
                "git",
                "gcp"
            ]
        },
        {
            "title": "Data Scientist",
            "matching_skills": [
                "sql",
                "python",
                "r",
                "git"
            ],
            "missing_skills": [
                "postgresql",
                "mysql",
                "gcp"
            ],
            "company_name": "Dyson3.0",
            "location": "Bangalore",
            "avg_base_pay_est": "#N/A",
            "company_rating": "3.0",
            "company_link": "https://glassdoor.co.in/partner/jobListing.htm?pos=219&ao=1136043&s=58&guid=00000187c7f8bed18a285e2ce6fd570e&src=GD_JOB_AD&t=SR&vt=w&cs=1_ecee3e6a&cb=1682687180763&jobListingId=1008613464006&jrtk=3-0-1gv3vhfngjfl1801-1gv3vhfo6ghqf800-01c184c6bd6ea631-",
            "time_since_posted": "24h",
            "company_skills": [
                "sql",
                "python",
                "r",
                "mysql",
                "postgresql",
                "git",
                "gcp"
            ]
        },
        ...
        ...
        ]
   
    

}
```
