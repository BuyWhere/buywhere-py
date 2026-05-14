"""BuyWhere Python SDK — official client for the BuyWhere Product Catalog API."""
from buywhere.async_client import AsyncBuyWhereClient
from buywhere.client import BuyWhereClient
from buywhere.exceptions import (
    APIError,
    AuthenticationError,
    BuyWhereError,
    NotFoundError,
    RateLimitError,
)
from buywhere.models import (
    AvailabilityInfo,
    Category,
    CategoryDetail,
    CompareProductItem,
    CompareProductsResponse,
    ComparisonSummary,
    DeliveryInfo,
    ImageInfo,
    InterpretedAs,
    Listing,
    MerchantInfo,
    NLQueryResponse,
    PriceCompareResponse,
    PriceInfo,
    PriceRange,
    Product,
    ReviewsSummary,
    SearchResponse,
    SearchResult,
)

__all__ = [
    "BuyWhereClient",
    "AsyncBuyWhereClient",
    # exceptions
    "BuyWhereError",
    "AuthenticationError",
    "NotFoundError",
    "RateLimitError",
    "APIError",
    # models
    "SearchResult",
    "SearchResponse",
    "Product",
    "PriceInfo",
    "MerchantInfo",
    "AvailabilityInfo",
    "DeliveryInfo",
    "ImageInfo",
    "ReviewsSummary",
    "Category",
    "CategoryDetail",
    "PriceCompareResponse",
    "Listing",
    "CompareProductItem",
    "CompareProductsResponse",
    "ComparisonSummary",
    "PriceRange",
    "InterpretedAs",
    "NLQueryResponse",
    # langchain (optional — requires buywhere-sdk[langchain])
    "BuyWhereTool",
]


def __getattr__(name: str) -> object:
    if name == "BuyWhereTool":
        from buywhere.tools import BuyWhereTool
        return BuyWhereTool
    raise AttributeError(f"module 'buywhere' has no attribute {name!r}")

__version__ = "0.2.0"
