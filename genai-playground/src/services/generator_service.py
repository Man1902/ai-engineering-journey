from models.request import GenerationRequest
from models.response import GenerationResponse
from providers.provider_factory import ProviderFactory


class GeneratorService:

    def generate(self, request: GenerationRequest) -> GenerationResponse:

        provider = ProviderFactory.get_provider(request.provider)

        return provider.generate(request)