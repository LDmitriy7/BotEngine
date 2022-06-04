import requests


class Tags:
    _a = '<a href="{url}">{text}</a>'
    _pre = '<pre>{}</pre>'
    _textarea = '<textarea cols="{cols}" rows="{rows}">{}</textarea>'

    def a(self, text: str, url: str):
        return self._a.format(text=text, url=url)

    def pre(self, text: str):
        return self._pre.format(text)

    def textarea(self, text: str = '', cols: str = '', rows: str = '', ):
        return self._textarea.format(text, cols=cols, rows=rows)


tags = Tags()


class ProjectsManagerError(Exception):
    pass


class ProjectsManager:
    def __init__(self, api_url: str):
        self.api_url = api_url
        self.session = requests.Session()

    def _request_get(self, endpoint: str) -> dict:
        url = self.api_url + endpoint
        resp = self.session.get(url)

        try:
            result = resp.json()
        except requests.exceptions.JSONDecodeError:
            raise ProjectsManagerError('Unknown error')

        if not result['ok']:
            raise ProjectsManagerError(result['error'])

        return result

    def _request_post(self, endpoint: str, params: dict) -> dict:
        url = self.api_url + endpoint
        resp = self.session.post(url, json=params)

        try:
            result = resp.json()
        except requests.exceptions.JSONDecodeError:
            raise ProjectsManagerError('Unknown error')

        if not result['ok']:
            raise ProjectsManagerError(result['error'])

        return result

    def projects(self) -> list[str]:
        result = self._request_get('/projects')
        return result['projects']

    def get(self, path: str) -> str | list:
        result = self._request_get(f'/get/{path}')

        if result['type'] == 'dir':
            return result['items']
        elif result['type'] == 'file':
            return result['text']

        raise ProjectsManagerError('Unknown item type')

    def edit(self, path: str, text: str):
        self._request_post(f'/edit/{path}', {'text': text})

    def deploy(self, project_name: str):
        self._request_get(f'/deploy/{project_name}')
