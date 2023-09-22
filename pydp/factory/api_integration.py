class APIIntegration:
    def fetch_data(self, endpoint: str) -> dict:
        pass


# Concrete integration classes for different APIs
class TwitterAPI(APIIntegration):
    def fetch_data(self, endpoint: str) -> dict:
        # Mock implementation for Twitter API
        return {'api': 'Twitter', 'data': f'Fetched from {endpoint}'}


class GitHubAPI(APIIntegration):
    def fetch_data(self, endpoint: str) -> dict:
        # Mock implementation for GitHub API
        return {'api': 'GitHub', 'data': f'Fetched from {endpoint}'}


class GoogleAPI(APIIntegration):
    def fetch_data(self, endpoint: str) -> dict:
        # Mock implementation for Google API
        return {'api': 'Google', 'data': f'Fetched from {endpoint}'}


# API Factory to create specific API integrations
class APIFactory:
    @staticmethod
    def create_integration(api_name: str) -> APIIntegration:
        if api_name == 'Twitter':
            return TwitterAPI()
        elif api_name == 'GitHub':
            return GitHubAPI()
        elif api_name == 'Google':
            return GoogleAPI()
        else:
            raise ValueError(f'Unknown API name: {api_name}')


# Usage
api_names = ['Twitter', 'GitHub', 'Google']
endpoint = '/sample_endpoint'
for api_name in api_names:
    integration = APIFactory.create_integration(api_name)
    print(integration.fetch_data(endpoint))
