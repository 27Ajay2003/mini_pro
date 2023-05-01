# API Reference

`server`: http://localhost:8000/

## Authenication APP Endpoints

desc:used for registering,login,viewing profile info of users and access token refresh

* [Register](docs/auth/register.md) : `/api/auth/register/`
* [Login](docs/auth/login.md) : `/api/auth/login/`
* [Profiles](docs/auth/profiles.md) : `/api/auth/profiles/`
* [User](docs/auth/user.md) : `/api/auth/user/`
* [Refresh](docs/auth/refresh.md) : `/api/auth/refresh/`

## JobScrape APP Endpoints

desc:used for searching the database and retrievel of scraped job results

* [Scrape_result](docs/jobs/scrape_result_pk.md) : `api/jobs/scrape-result/:pk`
* [Scrape_results](docs/jobs/scrape_results.md) : `api/jobs/scrape-results/`
* [Search](docs/jobs/search.md) : `/api/jobs/search/< >/?q=< >`



<!-- ## Endpoints that require Authentication

Closed endpoints require a valid Bearer Token to be included in the header of the request. 
A Token can be acquired from the Login view above.

### Current User related

Each endpoint manipulates or displays information related to the User whose
Token is provided with the request:

* [Show info](user/get.md) : `GET /api/user/`
* [Update info](user/put.md) : `PUT /api/user/`

### Account related

Endpoints for viewing and manipulating the Accounts that the Authenticated User
has permissions to access.

* [Show Accessible Accounts](accounts/get.md) : `GET /api/accounts/`
* [Create Account](accounts/post.md) : `POST /api/accounts/`
* [Show An Account](accounts/pk/get.md) : `GET /api/accounts/:pk/`
* [Update An Account](accounts/pk/put.md) : `PUT /api/accounts/:pk/`
* [Delete An Account](accounts/pk/delete.md) : `DELETE /api/accounts/:pk/` -->
