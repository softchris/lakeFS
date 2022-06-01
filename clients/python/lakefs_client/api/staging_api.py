"""
    lakeFS API

    lakeFS HTTP API  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Contact: services@treeverse.io
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from lakefs_client.api_client import ApiClient, Endpoint as _Endpoint
from lakefs_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from lakefs_client.model.error import Error
from lakefs_client.model.object_stats import ObjectStats
from lakefs_client.model.staging_location import StagingLocation
from lakefs_client.model.staging_metadata import StagingMetadata


class StagingApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_physical_address_endpoint = _Endpoint(
            settings={
                'response_type': (StagingLocation,),
                'auth': [
                    'basic_auth',
                    'cookie_auth',
                    'jwt_token',
                    'oidc_auth'
                ],
                'endpoint_path': '/repositories/{repository}/branches/{branch}/staging/backing',
                'operation_id': 'get_physical_address',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'repository',
                    'branch',
                    'path',
                ],
                'required': [
                    'repository',
                    'branch',
                    'path',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'repository':
                        (str,),
                    'branch':
                        (str,),
                    'path':
                        (str,),
                },
                'attribute_map': {
                    'repository': 'repository',
                    'branch': 'branch',
                    'path': 'path',
                },
                'location_map': {
                    'repository': 'path',
                    'branch': 'path',
                    'path': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.link_physical_address_endpoint = _Endpoint(
            settings={
                'response_type': (ObjectStats,),
                'auth': [
                    'basic_auth',
                    'cookie_auth',
                    'jwt_token',
                    'oidc_auth'
                ],
                'endpoint_path': '/repositories/{repository}/branches/{branch}/staging/backing',
                'operation_id': 'link_physical_address',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'repository',
                    'branch',
                    'path',
                    'staging_metadata',
                ],
                'required': [
                    'repository',
                    'branch',
                    'path',
                    'staging_metadata',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'repository':
                        (str,),
                    'branch':
                        (str,),
                    'path':
                        (str,),
                    'staging_metadata':
                        (StagingMetadata,),
                },
                'attribute_map': {
                    'repository': 'repository',
                    'branch': 'branch',
                    'path': 'path',
                },
                'location_map': {
                    'repository': 'path',
                    'branch': 'path',
                    'path': 'query',
                    'staging_metadata': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def get_physical_address(
        self,
        repository,
        branch,
        path,
        **kwargs
    ):
        """get a physical address and a return token to write object to underlying storage  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_physical_address(repository, branch, path, async_req=True)
        >>> result = thread.get()

        Args:
            repository (str):
            branch (str):
            path (str): relative to the branch

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            StagingLocation
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['repository'] = \
            repository
        kwargs['branch'] = \
            branch
        kwargs['path'] = \
            path
        return self.get_physical_address_endpoint.call_with_http_info(**kwargs)

    def link_physical_address(
        self,
        repository,
        branch,
        path,
        staging_metadata,
        **kwargs
    ):
        """associate staging on this physical address with a path  # noqa: E501

        If the supplied token matches the current staging token, associate the object as the physical address with the supplied path.  Otherwise, if staging has been committed and the token has expired, return a conflict and hint where to place the object to try again.  Caller should copy the object to the new physical address and PUT again with the new staging token.  (No need to back off, this is due to losing the race against a concurrent commit operation.)   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.link_physical_address(repository, branch, path, staging_metadata, async_req=True)
        >>> result = thread.get()

        Args:
            repository (str):
            branch (str):
            path (str): relative to the branch
            staging_metadata (StagingMetadata):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ObjectStats
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['repository'] = \
            repository
        kwargs['branch'] = \
            branch
        kwargs['path'] = \
            path
        kwargs['staging_metadata'] = \
            staging_metadata
        return self.link_physical_address_endpoint.call_with_http_info(**kwargs)

