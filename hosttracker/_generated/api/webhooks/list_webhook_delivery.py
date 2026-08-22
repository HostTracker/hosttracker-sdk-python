from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.insufficient_rights import InsufficientRights
from ...models.internal_error import InternalError
from ...models.invalid_cursor import InvalidCursor
from ...models.invalid_limit import InvalidLimit
from ...models.invalid_range import InvalidRange
from ...models.invalid_token import InvalidToken
from ...models.ip_not_allowed import IpNotAllowed
from ...models.list_webhook_delivery_event_item import (
    ListWebhookDeliveryEventItem,
)
from ...models.list_webhook_delivery_fields_item import (
    ListWebhookDeliveryFieldsItem,
)
from ...models.list_webhook_delivery_outcome_item import (
    ListWebhookDeliveryOutcomeItem,
)
from ...models.method_not_allowed import MethodNotAllowed
from ...models.missing_scope import MissingScope
from ...models.not_found import NotFound
from ...models.quota_exceeded import QuotaExceeded
from ...models.unknown_enum_value import UnknownEnumValue
from ...models.unknown_event_type import UnknownEventType
from ...models.unknown_field import UnknownField
from ...models.unknown_parameter import UnknownParameter
from ...models.webhook_delivery_page import WebhookDeliveryPage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    event: list[ListWebhookDeliveryEventItem] | Unset = UNSET,
    outcome: list[ListWebhookDeliveryOutcomeItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListWebhookDeliveryFieldsItem] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["from"] = from_

    params["to"] = to

    json_event: list[str] | Unset = UNSET
    if not isinstance(event, Unset):
        json_event = []
        for event_item_data in event:
            event_item: str = event_item_data
            json_event.append(event_item)

    params["event"] = json_event

    json_outcome: list[str] | Unset = UNSET
    if not isinstance(outcome, Unset):
        json_outcome = []
        for outcome_item_data in outcome:
            outcome_item: str = outcome_item_data
            json_outcome.append(outcome_item)

    params["outcome"] = json_outcome

    params["limit"] = limit

    params["cursor"] = cursor

    json_fields: list[str] | Unset = UNSET
    if not isinstance(fields, Unset):
        json_fields = []
        for fields_item_data in fields:
            fields_item: str = fields_item_data
            json_fields.append(fields_item)

    params["fields"] = json_fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/webhook/{id}/delivery".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | InvalidRange
    | UnknownEnumValue
    | UnknownEventType
    | UnknownField
    | UnknownParameter
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | WebhookDeliveryPage
    | None
):
    if response.status_code == 200:
        response_200 = WebhookDeliveryPage.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = InvalidToken.from_dict(response.json())

        return response_401

    if response.status_code == 403:

        def _parse_response_403(data: object) -> InsufficientRights | IpNotAllowed | MissingScope:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_403_type_0 = MissingScope.from_dict(data)

                return response_403_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_403_type_1 = InsufficientRights.from_dict(data)

                return response_403_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_403_type_2 = IpNotAllowed.from_dict(data)

            return response_403_type_2

        response_403 = _parse_response_403(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = NotFound.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = MethodNotAllowed.from_dict(response.json())

        return response_405

    if response.status_code == 422:

        def _parse_response_422(
            data: object,
        ) -> (
            InvalidCursor
            | InvalidLimit
            | InvalidRange
            | UnknownEnumValue
            | UnknownEventType
            | UnknownField
            | UnknownParameter
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_0 = UnknownField.from_dict(data)

                return response_422_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_1 = UnknownEventType.from_dict(data)

                return response_422_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_2 = InvalidCursor.from_dict(data)

                return response_422_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_3 = InvalidLimit.from_dict(data)

                return response_422_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_4 = InvalidRange.from_dict(data)

                return response_422_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_5 = UnknownEnumValue.from_dict(data)

                return response_422_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_422_type_6 = UnknownParameter.from_dict(data)

            return response_422_type_6

        response_422 = _parse_response_422(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = QuotaExceeded.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = InternalError.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | InvalidRange
    | UnknownEnumValue
    | UnknownEventType
    | UnknownField
    | UnknownParameter
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | WebhookDeliveryPage
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    event: list[ListWebhookDeliveryEventItem] | Unset = UNSET,
    outcome: list[ListWebhookDeliveryOutcomeItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListWebhookDeliveryFieldsItem] | Unset = UNSET,
) -> Response[
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | InvalidRange
    | UnknownEnumValue
    | UnknownEventType
    | UnknownField
    | UnknownParameter
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | WebhookDeliveryPage
]:
    """List recent deliveries for one webhook.

     Returns a page of recent deliveries for one webhook, each with its outcome, every attempt it took,
    the status code the endpoint answered and a short excerpt of its response - which is usually enough
    to see why a delivery failed. Filter by time window, event or outcome. A delivery that is still
    retrying reads as pending and carries the time of its next attempt. Deliveries are kept for a
    bounded window; the webhook's own record of its last delivery and failure count is always available.

    Args:
        id (UUID):
        from_ (int | Unset):
        to (int | Unset):
        event (list[ListWebhookDeliveryEventItem] | Unset):
        outcome (list[ListWebhookDeliveryOutcomeItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListWebhookDeliveryFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidCursor | InvalidLimit | InvalidRange | UnknownEnumValue | UnknownEventType | UnknownField | UnknownParameter | InvalidToken | MethodNotAllowed | NotFound | QuotaExceeded | WebhookDeliveryPage]
    """

    kwargs = _get_kwargs(
        id=id,
        from_=from_,
        to=to,
        event=event,
        outcome=outcome,
        limit=limit,
        cursor=cursor,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    *,
    client: AuthenticatedClient,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    event: list[ListWebhookDeliveryEventItem] | Unset = UNSET,
    outcome: list[ListWebhookDeliveryOutcomeItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListWebhookDeliveryFieldsItem] | Unset = UNSET,
) -> (
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | InvalidRange
    | UnknownEnumValue
    | UnknownEventType
    | UnknownField
    | UnknownParameter
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | WebhookDeliveryPage
    | None
):
    """List recent deliveries for one webhook.

     Returns a page of recent deliveries for one webhook, each with its outcome, every attempt it took,
    the status code the endpoint answered and a short excerpt of its response - which is usually enough
    to see why a delivery failed. Filter by time window, event or outcome. A delivery that is still
    retrying reads as pending and carries the time of its next attempt. Deliveries are kept for a
    bounded window; the webhook's own record of its last delivery and failure count is always available.

    Args:
        id (UUID):
        from_ (int | Unset):
        to (int | Unset):
        event (list[ListWebhookDeliveryEventItem] | Unset):
        outcome (list[ListWebhookDeliveryOutcomeItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListWebhookDeliveryFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidCursor | InvalidLimit | InvalidRange | UnknownEnumValue | UnknownEventType | UnknownField | UnknownParameter | InvalidToken | MethodNotAllowed | NotFound | QuotaExceeded | WebhookDeliveryPage
    """

    return sync_detailed(
        id=id,
        client=client,
        from_=from_,
        to=to,
        event=event,
        outcome=outcome,
        limit=limit,
        cursor=cursor,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    event: list[ListWebhookDeliveryEventItem] | Unset = UNSET,
    outcome: list[ListWebhookDeliveryOutcomeItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListWebhookDeliveryFieldsItem] | Unset = UNSET,
) -> Response[
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | InvalidRange
    | UnknownEnumValue
    | UnknownEventType
    | UnknownField
    | UnknownParameter
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | WebhookDeliveryPage
]:
    """List recent deliveries for one webhook.

     Returns a page of recent deliveries for one webhook, each with its outcome, every attempt it took,
    the status code the endpoint answered and a short excerpt of its response - which is usually enough
    to see why a delivery failed. Filter by time window, event or outcome. A delivery that is still
    retrying reads as pending and carries the time of its next attempt. Deliveries are kept for a
    bounded window; the webhook's own record of its last delivery and failure count is always available.

    Args:
        id (UUID):
        from_ (int | Unset):
        to (int | Unset):
        event (list[ListWebhookDeliveryEventItem] | Unset):
        outcome (list[ListWebhookDeliveryOutcomeItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListWebhookDeliveryFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidCursor | InvalidLimit | InvalidRange | UnknownEnumValue | UnknownEventType | UnknownField | UnknownParameter | InvalidToken | MethodNotAllowed | NotFound | QuotaExceeded | WebhookDeliveryPage]
    """

    kwargs = _get_kwargs(
        id=id,
        from_=from_,
        to=to,
        event=event,
        outcome=outcome,
        limit=limit,
        cursor=cursor,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    event: list[ListWebhookDeliveryEventItem] | Unset = UNSET,
    outcome: list[ListWebhookDeliveryOutcomeItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListWebhookDeliveryFieldsItem] | Unset = UNSET,
) -> (
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | InvalidRange
    | UnknownEnumValue
    | UnknownEventType
    | UnknownField
    | UnknownParameter
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | WebhookDeliveryPage
    | None
):
    """List recent deliveries for one webhook.

     Returns a page of recent deliveries for one webhook, each with its outcome, every attempt it took,
    the status code the endpoint answered and a short excerpt of its response - which is usually enough
    to see why a delivery failed. Filter by time window, event or outcome. A delivery that is still
    retrying reads as pending and carries the time of its next attempt. Deliveries are kept for a
    bounded window; the webhook's own record of its last delivery and failure count is always available.

    Args:
        id (UUID):
        from_ (int | Unset):
        to (int | Unset):
        event (list[ListWebhookDeliveryEventItem] | Unset):
        outcome (list[ListWebhookDeliveryOutcomeItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListWebhookDeliveryFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidCursor | InvalidLimit | InvalidRange | UnknownEnumValue | UnknownEventType | UnknownField | UnknownParameter | InvalidToken | MethodNotAllowed | NotFound | QuotaExceeded | WebhookDeliveryPage
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            from_=from_,
            to=to,
            event=event,
            outcome=outcome,
            limit=limit,
            cursor=cursor,
            fields=fields,
        )
    ).parsed
