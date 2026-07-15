# NI OSS SOURCE SNAPSHOT: nisystemlink-clients-python

<!--NI_OSS_SNAPSHOT repo=ni/nisystemlink-clients-python commit=0bed315df7e0dd210396f3669d42211c96a641d5 -->

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/tag/test_tagmanager.py sha256=395857f79cbfcd8cd6e9f16d0d21d3a011d8041d29217c09b2dfd31dfff18b2f bytes=113674 -->
## FILE: tests/tag/test_tagmanager.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/tag/test_tagmanager.py`
- sha256: `395857f79cbfcd8cd6e9f16d0d21d3a011d8041d29217c09b2dfd31dfff18b2f`
- bytes: 113674

````python
import asyncio
import time
import uuid
from collections import OrderedDict
from datetime import datetime, timedelta, timezone
from unittest import mock

import pytest  # type: ignore
from nisystemlink.clients import core, tag as tbase

from .http.httpclienttestbase import HttpClientTestBase, MockResponse
from ..anyorderlist import AnyOrderList


def _wait_for_call_count(mock_obj, expected: int, *, timeout: float = 3.0):
    """Wait until mock_obj.call_count >= expected or timeout.

    Args:
        mock_obj: Mock with call_count attribute.
        expected: Target call count (>=).
        timeout: Max seconds to wait.

    Returns:
        Elapsed seconds when condition satisfied.

    Raises:
        AssertionError on timeout or premature satisfaction.
    """
    start = time.monotonic()
    while True:
        if mock_obj.call_count >= expected:
            return time.monotonic() - start
        if time.monotonic() - start >= timeout:
            raise AssertionError(
                f"Timed out waiting for call_count >= {expected}. Final={mock_obj.call_count} timeout={timeout}s"
            )
        time.sleep(0.01)


class TestTagManager(HttpClientTestBase):
    def setup_method(self, method):
        super().setup_method(method)

        def get_client_mock(*args, **kwargs):
            return self._client

        with mock.patch(
            "nisystemlink.clients.tag._tag_manager.HttpClient", get_client_mock
        ):
            self._uut = tbase.TagManager(object())

    def test__metadata_supplied__create_selection__metadata_used_without_query(self):
        tags = [
            tbase.TagData("tag1"),
            tbase.TagData("tag2", tbase.DataType.BOOLEAN),
            tbase.TagData(
                "tag3", tbase.DataType.DATE_TIME, ["keyword1"], {"prop1": "value1"}
            ),
        ]

        selection = self._uut.create_selection(tags)

        assert self._client.all_requests.call_count == 0
        assert [t.path for t in tags] == sorted(selection.paths)
        assert tags == list(sorted(selection.metadata.values(), key=(lambda t: t.path)))
        assert [t.path for t in tags[1:]] == sorted(selection.values.keys())
        assert selection.values[tags[1].path].data_type == tbase.DataType.BOOLEAN
        assert selection.values[tags[2].path].data_type == tbase.DataType.DATE_TIME

    def test__open_selection__creates_selection_and_queries_tags(self):
        path1 = "tag1"
        path2 = "tag2"
        paths = [path1, path2]
        token = uuid.uuid4()

        def mock_request(method, uri, params=None, data=None):
            if (method, uri) == ("POST", "/nitag/v2/selections"):
                ret = dict(data) if data else {}
                ret["id"] = token
                return ret, MockResponse(method, uri)
            elif (method, uri) == ("GET", "/nitag/v2/selections/{id}/tags"):
                return (
                    [
                        {"type": "BOOLEAN", "path": path1},
                        {"type": "DOUBLE", "path": path2},
                    ],
                    MockResponse(method, uri),
                )
            elif (method, uri) == ("DELETE", "/nitag/v2/selections/{id}"):
                return None, MockResponse(method, uri)
            else:
                assert False, (method, uri)

        self._client.all_requests.configure_mock(side_effect=mock_request)

        selection = self._uut.open_selection(paths)

        assert self._client.all_requests.call_args_list == [
            mock.call(
                "POST",
                "/nitag/v2/selections",
                params=None,
                data={"searchPaths": AnyOrderList(paths)},
            ),
            mock.call("GET", "/nitag/v2/selections/{id}/tags", params={"id": token}),
        ]
        assert 2 == len(selection.metadata)

    @pytest.mark.asyncio
    async def test__open_selection_async__creates_selection_and_queries_tags(self):
        path1 = "tag1"
        path2 = "tag2"
        paths = [path1, path2]
        token = uuid.uuid4()

        def mock_request(method, uri, params=None, data=None):
            if (method, uri) == ("POST", "/nitag/v2/selections"):
                ret = dict(data) if data else {}
                ret["id"] = token
                return ret, MockResponse(method, uri)
            elif (method, uri) == ("GET", "/nitag/v2/selections/{id}/tags"):
                return (
                    [
                        {"type": "BOOLEAN", "path": path1},
                        {"type": "DOUBLE", "path": path2},
                    ],
                    MockResponse(method, uri),
                )
            elif (method, uri) == ("DELETE", "/nitag/v2/selections/{id}"):
                return None, MockResponse(method, uri)
            else:
                assert False, (method, uri)

        self._client.all_requests.configure_mock(side_effect=mock_request)

        selection = await self._uut.open_selection_async(paths)

        assert self._client.all_requests.call_args_list == [
            mock.call(
                "POST",
                "/nitag/v2/selections",
                params=None,
                data={"searchPaths": AnyOrderList(paths)},
            ),
            mock.call("GET", "/nitag/v2/selections/{id}/tags", params={"id": token}),
        ]
        assert 2 == len(selection.metadata)

    def test__bag_arguments__open__raises(self):
        with pytest.raises(ValueError):
            self._uut.open(None)
        with pytest.raises(ValueError):
            self._uut.open(None, tbase.DataType.BOOLEAN)
        with pytest.raises(ValueError):
            self._uut.open(None, tbase.DataType.BOOLEAN, create=True)
        with pytest.raises(ValueError):
            self._uut.open("")
        with pytest.raises(ValueError):
            self._uut.open("", tbase.DataType.BOOLEAN)
        with pytest.raises(ValueError):
            self._uut.open("", tbase.DataType.BOOLEAN, create=True)
        with pytest.raises(ValueError):
            self._uut.open(" ")
        with pytest.raises(ValueError):
            self._uut.open(" ", tbase.DataType.BOOLEAN)
        with pytest.raises(ValueError):
            self._uut.open(" ", tbase.DataType.BOOLEAN, create=True)
        with pytest.raises(ValueError):
            self._uut.open("*")
        with pytest.raises(ValueError):
            self._uut.open("*", tbase.DataType.BOOLEAN)
        with pytest.raises(ValueError):
            self._uut.open("*", tbase.DataType.BOOLEAN, create=True)
        with pytest.raises(ValueError):
            self._uut.open("tag", tbase.DataType.UNKNOWN)
        with pytest.raises(ValueError):
            self._uut.open("tag", tbase.DataType.UNKNOWN, create=True)

    def test__existing_tag__open_without_datatype__retrieves_tag(self):
        path = "tag1"
        public_properties = {"prop1": "value1", "prop2": "value2"}
        all_properties = dict(public_properties)
        dummy_tag = tbase.TagData(path)
        dummy_tag.retention_type = tbase.RetentionType.COUNT
        dummy_tag.retention_count = 7
        dummy_tag.retention_days = 9
        dummy_tag._copy_retention_properties(all_properties)
        keywords = ["keyword1", "keyword2"]
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(
                [
                    {
                        "type": "BOOLEAN",
                        "properties": all_properties,
                        "path": path,
                        "keywords": keywords,
                        "collectAggregates": True,
                    }
                ]
            )
        )

        tag = self._uut.open(path)

        self._client.all_requests.assert_called_once_with(
            "GET", "/nitag/v2/tags/{path}", params={"path": path}
        )
        assert tag is not None
        assert tbase.DataType.BOOLEAN == tag.data_type
        assert tag.collect_aggregates is True
        assert keywords == sorted(tag.keywords)
        assert sorted(public_properties.items()) == sorted(tag.properties.items())
        assert dummy_tag.retention_count == tag.retention_count
        assert dummy_tag.retention_days == tag.retention_days
        assert dummy_tag.retention_type == tag.retention_type

    def test___tag_not_found__open_without_datatype__raises(self):
        err = core.ApiError(name="Tag.NoSuchTag")
        ex = core.ApiException("404 tag not found", err)
        self._client.all_requests.configure_mock(side_effect=ex)

        with pytest.raises(core.ApiException) as actual:
            self._uut.open("tag")
        assert ex is actual.value

        self._client.all_requests.assert_called_once_with(
            "GET", "/nitag/v2/tags/{path}", params={"path": "tag"}
        )

    def test___tag_not_found__open_with_datatype__creates_tag(self):
        path = "tag"
        err = core.ApiError(name="Tag.NoSuchTag")
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(
                [core.ApiException("404 tag not found", err), None]
            )
        )

        tag = self._uut.open(path, tbase.DataType.UINT64)

        assert self._client.all_requests.call_args_list == [
            mock.call("GET", "/nitag/v2/tags/{path}", params={"path": "tag"}),
            mock.call(
                "POST",
                "/nitag/v2/tags",
                params=None,
                data={"path": path, "type": "U_INT64"},
            ),
        ]
        assert path == tag.path
        assert tbase.DataType.UINT64 == tag.data_type
        assert not tag.collect_aggregates
        assert 0 == len(tag.keywords)
        assert 0 == len(tag.properties)
        assert tag.retention_count is None
        assert tag.retention_days is None
        assert tbase.RetentionType.NONE == tag.retention_type

    def test___tag_not_found__open_with_create_true__creates_tag(self):
        path = "tag"
        err = core.ApiError(name="Tag.NoSuchTag")
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(
                [core.ApiException("404 tag not found", err), None]
            )
        )

        tag = self._uut.open(path, tbase.DataType.UINT64, create=True)

        assert self._client.all_requests.call_args_list == [
            mock.call("GET", "/nitag/v2/tags/{path}", params={"path": "tag"}),
            mock.call(
                "POST",
                "/nitag/v2/tags",
                params=None,
                data={"path": path, "type": "U_INT64"},
            ),
        ]
        assert path == tag.path
        assert tbase.DataType.UINT64 == tag.data_type
        assert not tag.collect_aggregates
        assert 0 == len(tag.keywords)
        assert 0 == len(tag.properties)
        assert tag.retention_count is None
        assert tag.retention_days is None
        assert tbase.RetentionType.NONE == tag.retention_type

    def test__tag_exists__open__does_not_create_tag(self):
        path = "tag1"
        public_properties = {"prop1": "value1", "prop2": "value2"}
        all_properties = dict(public_properties)
        dummy_tag = tbase.TagData(path)
        dummy_tag.retention_type = tbase.RetentionType.COUNT
        dummy_tag.retention_count = 7
        dummy_tag.retention_days = 9
        dummy_tag._copy_retention_properties(all_properties)
        keywords = ["keyword1", "keyword2"]
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(
                [
                    {
                        "type": "BOOLEAN",
                        "properties": all_properties,
                        "path": path,
                        "keywords": keywords,
                        "collectAggregates": True,
                    }
                ]
            )
        )

        tag = self._uut.open(path, tbase.DataType.BOOLEAN, create=True)

        self._client.all_requests.assert_called_once_with(
            "GET", "/nitag/v2/tags/{path}", params={"path": "tag1"}
        )
        assert tag is not None
        assert tbase.DataType.BOOLEAN == tag.data_type
        assert tag.collect_aggregates is True
        assert keywords == sorted(tag.keywords)
        assert sorted(public_properties.items()) == sorted(tag.properties.items())
        assert dummy_tag.retention_count == tag.retention_count
        assert dummy_tag.retention_days == tag.retention_days
        assert dummy_tag.retention_type == tag.retention_type

    def test__tag_not_found__open_with_create_False__raises(self):
        err = core.ApiError(name="Tag.NoSuchTag")
        ex = core.ApiException("404 tag not found", err)
        self._client.all_requests.configure_mock(side_effect=ex)

        with pytest.raises(core.ApiException) as actual:
            self._uut.open("tag", tbase.DataType.DOUBLE, create=False)
        assert ex is actual.value

        self._client.all_requests.assert_called_once_with(
            "GET", "/nitag/v2/tags/{path}", params={"path": "tag"}
        )

    def test__tag_exists_with_different_datatype__open__raises(self):
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request([{"type": "BOOLEAN", "path": "tag"}] * 3)
        )
        with pytest.raises(core.ApiException):
            self._uut.open("tag", tbase.DataType.DOUBLE)
        with pytest.raises(core.ApiException):
            self._uut.open("tag", tbase.DataType.DOUBLE, create=False)
        with pytest.raises(core.ApiException):
            self._uut.open("tag", tbase.DataType.DOUBLE, create=True)

        assert self._client.all_requests.call_args_list == [
            mock.call("GET", "/nitag/v2/tags/{path}", params={"path": "tag"}),
            mock.call("GET", "/nitag/v2/tags/{path}", params={"path": "tag"}),
            mock.call("GET", "/nitag/v2/tags/{path}", params={"path": "tag"}),
        ]

    @pytest.mark.asyncio
    async def test__bag_arguments__open_async__raises(self):
        with pytest.raises(ValueError):
            await self._uut.open_async(None)
        with pytest.raises(ValueError):
            await self._uut.open_async(None, tbase.DataType.BOOLEAN)
        with pytest.raises(ValueError):
            await self._uut.open_async(None, tbase.DataType.BOOLEAN, create=True)
        with pytest.raises(ValueError):
            await self._uut.open_async("")
        with pytest.raises(ValueError):
            await self._uut.open_async("", tbase.DataType.BOOLEAN)
        with pytest.raises(ValueError):
            await self._uut.open_async("", tbase.DataType.BOOLEAN, create=True)
        with pytest.raises(ValueError):
            await self._uut.open_async(" ")
        with pytest.raises(ValueError):
            await self._uut.open_async(" ", tbase.DataType.BOOLEAN)
        with pytest.raises(ValueError):
            await self._uut.open_async(" ", tbase.DataType.BOOLEAN, create=True)
        with pytest.raises(ValueError):
            await self._uut.open_async("*")
        with pytest.raises(ValueError):
            await self._uut.open_async("*", tbase.DataType.BOOLEAN)
        with pytest.raises(ValueError):
            await self._uut.open_async("*", tbase.DataType.BOOLEAN, create=True)
        with pytest.raises(ValueError):
            await self._uut.open_async("tag", tbase.DataType.UNKNOWN)
        with pytest.raises(ValueError):
            await self._uut.open_async("tag", tbase.DataType.UNKNOWN, create=True)

    @pytest.mark.asyncio
    async def test__existing_tag__open_async_without_datatype__retrieves_tag(self):
        path = "tag1"
        public_properties = {"prop1": "value1", "prop2": "value2"}
        all_properties = dict(public_properties)
        dummy_tag = tbase.TagData(path)
        dummy_tag.retention_type = tbase.RetentionType.COUNT
        dummy_tag.retention_count = 7
        dummy_tag.retention_days = 9
        dummy_tag._copy_retention_properties(all_properties)
        keywords = ["keyword1", "keyword2"]
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(
                [
                    {
                        "type": "BOOLEAN",
                        "properties": all_properties,
                        "path": path,
                        "keywords": keywords,
                        "collectAggregates": True,
                    }
                ]
            )
        )

        tag = await self._uut.open_async(path)

        self._client.all_requests.assert_called_once_with(
            "GET", "/nitag/v2/tags/{path}", params={"path": "tag1"}
        )
        assert tag is not None
        assert tbase.DataType.BOOLEAN == tag.data_type
        assert tag.collect_aggregates is True
        assert keywords == sorted(tag.keywords)
        assert sorted(public_properties.items()) == sorted(tag.properties.items())
        assert dummy_tag.retention_count == tag.retention_count
        assert dummy_tag.retention_days == tag.retention_days
        assert dummy_tag.retention_type == tag.retention_type

    @pytest.mark.asyncio
    async def test___tag_not_found__open_async_without_datatype__raises(self):
        err = core.ApiError(name="Tag.NoSuchTag")
        ex = core.ApiException("404 tag not found", err)
        self._client.all_requests.configure_mock(side_effect=ex)

        with pytest.raises(core.ApiException) as actual:
            await self._uut.open_async("tag")
        assert ex is actual.value

        self._client.all_requests.assert_called_once_with(
            "GET", "/nitag/v2/tags/{path}", params={"path": "tag"}
        )

    @pytest.mark.asyncio
    async def test___tag_not_found__open_async_with_datatype__creates_tag(self):
        path = "tag"
        err = core.ApiError(name="Tag.NoSuchTag")
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(
                [core.ApiException("404 tag not found", err), None]
            )
        )

        tag = await self._uut.open_async(path, tbase.DataType.UINT64)

        assert self._client.all_requests.call_args_list == [
            mock.call("GET", "/nitag/v2/tags/{path}", params={"path": "tag"}),
            mock.call(
                "POST",
                "/nitag/v2/tags",
                params=None,
                data={"path": path, "type": "U_INT64"},
            ),
        ]
        assert path == tag.path
        assert tbase.DataType.UINT64 == tag.data_type
        assert not tag.collect_aggregates
        assert 0 == len(tag.keywords)
        assert 0 == len(tag.properties)
        assert tag.retention_count is None
        assert tag.retention_days is None
        assert tbase.RetentionType.NONE == tag.retention_type

    @pytest.mark.asyncio
    async def test___tag_not_found__open_async_with_create_true__creates_tag(self):
        path = "tag"
        err = core.ApiError(name="Tag.NoSuchTag")
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(
                [core.ApiException("404 tag not found", err), None]
            )
        )

        tag = await self._uut.open_async(path, tbase.DataType.UINT64, create=True)

        assert self._client.all_requests.call_args_list == [
            mock.call("GET", "/nitag/v2/tags/{path}", params={"path": "tag"}),
            mock.call(
                "POST",
                "/nitag/v2/tags",
                params=None,
                data={"path": path, "type": "U_INT64"},
            ),
        ]
        assert path == tag.path
        assert tbase.DataType.UINT64 == tag.data_type
        assert not tag.collect_aggregates
        assert 0 == len(tag.keywords)
        assert 0 == len(tag.properties)
        assert tag.retention_count is None
        assert tag.retention_days is None
        assert tbase.RetentionType.NONE == tag.retention_type

    @pytest.mark.asyncio
    async def test__tag_exists__open_async__does_not_create_tag(self):
        path = "tag1"
        public_properties = {"prop1": "value1", "prop2": "value2"}
        all_properties = dict(public_properties)
        dummy_tag = tbase.TagData(path)
        dummy_tag.retention_type = tbase.RetentionType.COUNT
        dummy_tag.retention_count = 7
        dummy_tag.retention_days = 9
        dummy_tag._copy_retention_properties(all_properties)
        keywords = ["keyword1", "keyword2"]
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(
                [
                    {
                        "type": "BOOLEAN",
                        "properties": all_properties,
                        "path": path,
                        "keywords": keywords,
                        "collectAggregates": True,
                    }
                ]
            )
        )

        tag = await self._uut.open_async(path, tbase.DataType.BOOLEAN, create=True)

        self._client.all_requests.assert_called_once_with(
            "GET", "/nitag/v2/tags/{path}", params={"path": "tag1"}
        )
        assert tag is not None
        assert tbase.DataType.BOOLEAN == tag.data_type
        assert tag.collect_aggregates is True
        assert keywords == sorted(tag.keywords)
        assert sorted(public_properties.items()) == sorted(tag.properties.items())
        assert dummy_tag.retention_count == tag.retention_count
        assert dummy_tag.retention_days == tag.retention_days
        assert dummy_tag.retention_type == tag.retention_type

    @pytest.mark.asyncio
    async def test__tag_not_found__open_async_with_create_False__raises(self):
        err = core.ApiError(name="Tag.NoSuchTag")
        ex = core.ApiException("404 tag not found", err)
        self._client.all_requests.configure_mock(side_effect=ex)

        with pytest.raises(core.ApiException) as actual:
            await self._uut.open_async("tag", tbase.DataType.DOUBLE, create=False)
        assert ex is actual.value

        self._client.all_requests.assert_called_once_with(
            "GET", "/nitag/v2/tags/{path}", params={"path": "tag"}
        )

    @pytest.mark.asyncio
    async def test__tag_exists_with_different_datatype__open_async__raises(self):
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request([{"type": "BOOLEAN", "path": "tag"}] * 3)
        )
        with pytest.raises(core.ApiException):
            await self._uut.open_async("tag", tbase.DataType.DOUBLE)
        with pytest.raises(core.ApiException):
            await self._uut.open_async("tag", tbase.DataType.DOUBLE, create=False)
        with pytest.raises(core.ApiException):
            await self._uut.open_async("tag", tbase.DataType.DOUBLE, create=True)

        assert self._client.all_requests.call_args_list == [
            mock.call("GET", "/nitag/v2/tags/{path}", params={"path": "tag"}),
            mock.call("GET", "/nitag/v2/tags/{path}", params={"path": "tag"}),
            mock.call("GET", "/nitag/v2/tags/{path}", params={"path": "tag"}),
        ]

    def test__invalid_tags__refresh__raises(self):
        with pytest.raises(ValueError):
            self._uut.refresh(None)
        with pytest.raises(ValueError):
            self._uut.refresh([None])
        with pytest.raises(ValueError):
            self._uut.refresh([tbase.TagData("tag"), None])
        with pytest.raises(ValueError):
            self._uut.refresh([tbase.TagData("tag"), tbase.TagData(None)])
        with pytest.raises(ValueError):
            self._uut.refresh([tbase.TagData("tag"), tbase.TagData("")])

    def test__multiple_tags_given__refresh__all_tags_updated(self):
        path1 = "tag1"
        path2 = "tag2"
        public_properties = {"prop1": "value1", "prop2": "value2"}
        all_properties = dict(public_properties)
        dummy_tag = tbase.TagData(path1)
        dummy_tag.retention_type = tbase.RetentionType.COUNT
        dummy_tag.retention_count = 7
        dummy_tag.retention_days = 9
        dummy_tag._copy_retention_properties(all_properties)
        keywords = ["keyword1", "keyword2"]
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(
                [
                    {
                        "totalCount": 2,
                        "tags": [
                            {
                                "type": "BOOLEAN",
                                "properties": all_properties,
                                "path": path1,
                                "keywords": keywords,
                                "collectAggregates": True,
                            },
                            {"type": "DOUBLE", "path": path2},
                        ],
                    }
                ]
            )
        )
        tag1 = tbase.TagData(path1)
        tag2 = tbase.TagData(
            path2, tbase.DataType.UINT64, ["dummy"], {"dummy": "dummy"}
        )
        tag2.set_retention_count(9)

        self._uut.refresh([tag1, tag2])

        self._client.all_requests.assert_called_once_with(
            "GET", "/nitag/v2/tags", params={"path": path1 + "," + path2, "take": "2"}
        )
        assert tbase.DataType.BOOLEAN == tag1.data_type
        assert tag1.collect_aggregates is True
        assert keywords == sorted(tag1.keywords)
        assert sorted(public_properties.items()) == sorted(tag1.properties.items())
        assert dummy_tag.retention_count == tag1.retention_count
        assert dummy_tag.retention_days == tag1.retention_days
        assert dummy_tag.retention_type == tag1.retention_type

        assert tbase.DataType.DOUBLE == tag2.data_type
        assert tag2.collect_aggregates is False
        assert 0 == len(tag2.keywords)
        assert 0 == len(tag2.properties)
        assert tag2.retention_count is None
        assert tag2.retention_days is None
        assert tbase.RetentionType.NONE == tag2.retention_type

    def test__missing_tags_supplied__refresh__missing_tags_ignored(self):
        keywords = ["keyword"]
        properties = {"prop": "value"}
        tag1 = tbase.TagData("existing")
        tag2 = tbase.TagData("missing", tbase.DataType.DOUBLE, keywords, properties)
        tag2.collect_aggregates = True
        tag2.set_retention_days(6)
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(
                [{"totalCount": 1, "tags": [{"type": "BOOLEAN", "path": "existing"}]}]
            )
        )

        self._uut.refresh([tag1, tag2])

        self._client.all_requests.assert_called_once_with(
            "GET", "/nitag/v2/tags", params={"path": "existing,missing", "take": "2"}
        )
        assert tbase.DataType.BOOLEAN == tag1.data_type
        assert tbase.DataType.UNKNOWN == tag2.data_type
        assert tag2.collect_aggregates is True
        assert keywords == tag2.keywords
        assert properties == tag2.properties
        assert tag2.retention_count is None
        assert 6 == tag2.retention_days
        assert tbase.RetentionType.DURATION == tag2.retention_type

    @pytest.mark.asyncio
    async def test__invalid_tags__refresh_async__raises(self):
        with pytest.raises(ValueError):
            await self._uut.refresh_async(None)
        with pytest.raises(ValueError):
            await self._uut.refresh_async([None])
        with pytest.raises(ValueError):
            await self._uut.refresh_async([tbase.TagData("tag"), None])
        with pytest.raises(ValueError):
            await self._uut.refresh_async([tbase.TagData("tag"), tbase.TagData(None)])
        with pytest.raises(ValueError):
            await self._uut.refresh_async([tbase.TagData("tag"), tbase.TagData("")])

    @pytest.mark.asyncio
    async def test__multiple_tags_given__refresh_async__all_tags_updated(self):
        path1 = "tag1"
        path2 = "tag2"
        public_properties = {"prop1": "value1", "prop2": "value2"}
        all_properties = dict(public_properties)
        dummy_tag = tbase.TagData(path1)
        dummy_tag.retention_type = tbase.RetentionType.COUNT
        dummy_tag.retention_count = 7
        dummy_tag.retention_days = 9
        dummy_tag._copy_retention_properties(all_properties)
        keywords = ["keyword1", "keyword2"]
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(
                [
                    {
                        "totalCount": 2,
                        "tags": [
                            {
                                "type": "BOOLEAN",
                                "properties": all_properties,
                                "path": path1,
                                "keywords": keywords,
                                "collectAggregates": True,
                            },
                            {"type": "DOUBLE", "path": path2},
                        ],
                    }
                ]
            )
        )

        tag1 = tbase.TagData(path1)
        tag2 = tbase.TagData(
            path2, tbase.DataType.UINT64, ["dummy"], {"dummy": "dummy"}
        )
        tag2.set_retention_count(9)
        await self._uut.refresh_async([tag1, tag2])

        self._client.all_requests.assert_called_once_with(
            "GET", "/nitag/v2/tags", params={"path": path1 + "," + path2, "take": "2"}
        )
        assert tbase.DataType.BOOLEAN == tag1.data_type
        assert tag1.collect_aggregates is True
        assert keywords == sorted(tag1.keywords)
        assert sorted(public_properties.items()) == sorted(tag1.properties.items())
        assert dummy_tag.retention_count == tag1.retention_count
        assert dummy_tag.retention_days == tag1.retention_days
        assert dummy_tag.retention_type == tag1.retention_type

        assert tbase.DataType.DOUBLE == tag2.data_type
        assert tag2.collect_aggregates is False
        assert 0 == len(tag2.keywords)
        assert 0 == len(tag2.properties)
        assert tag2.retention_count is None
        assert tag2.retention_days is None
        assert tbase.RetentionType.NONE == tag2.retention_type

    @pytest.mark.asyncio
    async def test__missing_tags_supplied__refresh_async__missing_tags_ignored(self):
        keywords = ["keyword"]
        properties = {"prop": "value"}
        tag1 = tbase.TagData("existing")
        tag2 = tbase.TagData("missing", tbase.DataType.DOUBLE, keywords, properties)
        tag2.collect_aggregates = True
        tag2.set_retention_days(6)
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(
                [{"totalCount": 1, "tags": [{"type": "BOOLEAN", "path": "existing"}]}]
            )
        )

        await self._uut.refresh_async([tag1, tag2])

        self._client.all_requests.assert_called_once_with(
            "GET", "/nitag/v2/tags", params={"path": "existing,missing", "take": "2"}
        )
        assert tbase.DataType.BOOLEAN == tag1.data_type
        assert tbase.DataType.UNKNOWN == tag2.data_type
        assert tag2.collect_aggregates is True
        assert keywords == tag2.keywords
        assert properties == tag2.properties
        assert tag2.retention_count is None
        assert 6 == tag2.retention_days
        assert tbase.RetentionType.DURATION == tag2.retention_type

    def test__bad_arguments__query__raises(self):
        with pytest.raises(ValueError):
            self._uut.query(skip=-1, take=0)
        with pytest.raises(ValueError):
            self._uut.query(skip=0, take=-1)

        with pytest.raises(ValueError):
            self._uut.query([])
        with pytest.raises(ValueError):
            self._uut.query(["tag", None])
        with pytest.raises(ValueError):
            self._uut.query(["tag", ""])
        with pytest.raises(ValueError):
            self._uut.query(["tag", " "])

        with pytest.raises(ValueError):
            self._uut.query([], skip=0, take=0)
        with pytest.raises(ValueError):
            self._uut.query(["tag", None], skip=0, take=0)
        with pytest.raises(ValueError):
            self._uut.query(["tag", ""], skip=0, take=0)
        with pytest.raises(ValueError):
            self._uut.query(["tag", " "], skip=0, take=0)
        with pytest.raises(ValueError):
            self._uut.query(["tag"], skip=-1, take=0)
        with pytest.raises(ValueError):
            self._uut.query(["tag"], skip=0, take=-1)

        with pytest.raises(ValueError):
            self._uut.query(["tag", None], None, None)
        with pytest.raises(ValueError):
            self._uut.query(["tag", ""], None, None)
        with pytest.raises(ValueError):
            self._uut.query(["tag", " "], None, None)

        with pytest.raises(ValueError):
            self._uut.query(["tag", None], None, None, skip=0, take=0)
        with pytest.raises(ValueError):
            self._uut.query(["tag", ""], None, None, skip=0, take=0)
        with pytest.raises(ValueError):
            self._uut.query(["tag", " "], None, None, skip=0, take=0)
        with pytest.raises(ValueError):
            self._uut.query(["tag"], None, None, skip=-1, take=0)
        with pytest.raises(ValueError):
            self._uut.query(["tag"], None, None, skip=0, take=-1)

    def test__only_skip_and_take_supplied__query__performs_query(self):
        total_count = 4
        path1 = "tag1"
        path2 = "tag2"
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(
                [
                    {
                        "totalCount": total_count,
                        "tags": [{"type": "BOOLEAN", "path": path1}],
                    },
                    {
                        "totalCount": total_count,
                        "tags": [{"type": "DATE_TIME", "path": path2}],
                    },
                ]
            )
        )

        result = self._uut.query(skip=2, take=1)

        assert total_count == result.total_count
        self._client.all_requests.assert_called_once_with(
            "GET", "/nitag/v2/tags", params={"skip": "2", "take": "1"}
        )
        pages = list(result)

        assert self._client.all_requests.call_args_list == [
            mock.call("GET", "/nitag/v2/tags", params={"skip": "2", "take": "1"}),
            mock.call("GET", "/nitag/v2/tags", params={"skip": "3", "take": "1"}),
        ]

        assert 2 == len(pages)
        assert 1 == len(pages[0])
        assert path1 == pages[0][0].path
        assert tbase.DataType.BOOLEAN == pages[0][0].data_type
        assert 1 == len(pages[1])
        assert path2 == pages[1][0].path
        assert tbase.DataType.DATE_TIME == pages[1][0].data_type

    def test__only_paths_supplied__query__performs_query(self):
        total_count = 0
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request([{"totalCount": 0, "tags": []}])
        )

        result = self._uut.query(["tag1", "tag2"])

        assert total_count == result.total_count
        self._client.all_requests.assert_called_once_with(
            "GET", "/nitag/v2/tags", params={"path": "tag1,tag2", "skip": "0"}
        )

    def test__path_with_skip_and_take_supplied__query__performs_query(self):
        total_count = 4
        path1 = "tag1"
        path2 = "tag2"
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(
                [
                    {
                        "totalCount": total_count,
                        "tags": [{"type": "BOOLEAN", "path": path1}],
                    },
                    {
                        "totalCount": total_count,
                        "tags": [{"type": "DATE_TIME", "path": path2}],
                    },
                ]
            )
        )

        result = self._uut.query(
            ["missing1", path1, "missing2", path2, "missing3"], skip=2, take=1
        )
        assert total_count == result.total_count
        paths = ",".join(("missing1", path1, "missing2", path2, "missing3"))
        self._client.all_requests.assert_called_once_with(
            "GET", "/nitag/v2/tags", params={"path": paths, "skip": "2", "take": "1"}
        )

        pages = list(result)
        assert self._client.all_requests.call_args_list == [
            mock.call(
                "GET",
                "/nitag/v2/tags",
                params={"path": paths, "skip": "2", "take": "1"},
            ),
            mock.call(
                "GET",
                "/nitag/v2/tags",
                params={"path": paths, "skip": "3", "take": "1"},
            ),
        ]

        assert 2 == len(pages)
        assert 1 == len(pages[0])
        assert path1 == pages[0][0].path
        assert tbase.DataType.BOOLEAN == pages[0][0].data_type
        assert 1 == len(pages[1])
        assert path2 == pages[1][0].path
        assert tbase.DataType.DATE_TIME == pages[1][0].data_type

    def test__paths_with_keywords_and_properties_supplied__query__performs_query(self):
        total_count = 0
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(
                [{"totalCount": total_count, "tags": []}]
            )
        )

        result = self._uut.query(
            ["tag1", "tag2"],
            ["keyword1", "keyword2"],
            OrderedDict((("prop1", "value1"), ("prop2", "value2"))),
        )

        assert total_count == result.total_count
        self._client.all_requests.assert_called_once_with(
            "GET",
            "/nitag/v2/tags",
            params={
                "path": "tag1,tag2",
                "keywords": "keyword1,keyword2",
                "properties": "prop1=value1,prop2=value2",
                "skip": "0",
            },
        )

    def test__only_keywords_and_properties_supplied__query__performs_query(self):
        total_count = 0
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(
                [{"totalCount": total_count, "tags": []}]
            )
        )

        result = self._uut.query(
            None,
            ["keyword1", "keyword2"],
            OrderedDict((("prop1", "value1"), ("prop2", "value2"))),
        )

        assert total_count == result.total_count
        self._client.all_requests.assert_called_once_with(
            "GET",
            "/nitag/v2/tags",
            params={
                "keywords": "keyword1,keyword2",
                "properties": "prop1=value1,prop2=value2",
                "skip": "0",
            },
        )

    def test__all_inputs_supplied__query__performs_query(self):
        total_count = 4
        path1 = "tag1"
        path2 = "tag2"
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(
                [
                    {
                        "totalCount": total_count,
                        "tags": [{"type": "BOOLEAN", "path": path1}],
                    },
                    {
                        "totalCount": total_count,
                        "tags": [{"type": "DATE_TIME", "path": path2}],
                    },
                ]
            )
        )

        result = self._uut.query(
            ["missing1", path1, "missing2", path2, "missing3"],
            ["keyword1", "keyword2"],
            OrderedDict((("prop1", "value1"), ("prop2", "value2"))),
            skip=2,
            take=1,
        )
        assert total_count == result.total_count
        paths = ",".join(("missing1", path1, "missing2", path2, "missing3"))
        self._client.all_requests.assert_called_once_with(
            "GET",
            "/nitag/v2/tags",
            params={
                "path": paths,
                "keywords": "keyword1,keyword2",
                "properties": "prop1=value1,prop2=value2",
                "skip": "2",
                "take": "1",
            },
        )

        pages = list(result)
        assert self._client.all_requests.call_args_list == [
            mock.call(
                "GET",
                "/nitag/v2/tags",
                params={
                    "path": paths,
                    "keywords": "keyword1,keyword2",
                    "properties": "prop1=value1,prop2=value2",
                    "skip": "2",
                    "take": "1",
                },
            ),
            mock.call(
                "GET",
                "/nitag/v2/tags",
                params={
                    "path": paths,
                    "keywords": "keyword1,keyword2",
                    "properties": "prop1=value1,prop2=value2",
                    "skip": "3",
                    "take": "1",
                },
            ),
        ]

        assert 2 == len(pages)
        assert 1 == len(pages[0])
        assert path1 == pages[0][0].path
        assert tbase.DataType.BOOLEAN == pages[0][0].data_type
        assert 1 == len(pages[1])
        assert path2 == pages[1][0].path
        assert tbase.DataType.DATE_TIME == pages[1][0].data_type

    @pytest.mark.asyncio
    async def test__bad_arguments__query_async__raises(self):
        with pytest.raises(ValueError):
            await self._uut.query_async(skip=-1, take=0)
        with pytest.raises(ValueError):
            await self._uut.query_async(skip=0, take=-1)

        with pytest.raises(ValueError):
            await self._uut.query_async([])
        with pytest.raises(ValueError):
            await self._uut.query_async(["tag", None])
        with pytest.raises(ValueError):
            await self._uut.query_async(["tag", ""])
        with pytest.raises(ValueError):
            await self._uut.query_async(["tag", " "])

        with pytest.raises(ValueError):
            await self._uut.query_async([], skip=0, take=0)
        with pytest.raises(ValueError):
            await self._uut.query_async(["tag", None], skip=0, take=0)
        with pytest.raises(ValueError):
            await self._uut.query_async(["tag", ""], skip=0, take=0)
        with pytest.raises(ValueError):
            await self._uut.query_async(["tag", " "], skip=0, take=0)
        with pytest.raises(ValueError):
            await self._uut.query_async(["tag"], skip=-1, take=0)
        with pytest.raises(ValueError):
            await self._uut.query_async(["tag"], skip=0, take=-1)

        with pytest.raises(ValueError):
            await self._uut.query_async(["tag", None], None, None)
        with pytest.raises(ValueError):
            await self._uut.query_async(["tag", ""], None, None)
        with pytest.raises(ValueError):
            await self._uut.query_async(["tag", " "], None, None)

        with pytest.raises(ValueError):
            await self._uut.query_async(["tag", None], None, None, skip=0, take=0)
        with pytest.raises(ValueError):
            await self._uut.query_async(["tag", ""], None, None, skip=0, take=0)
        with pytest.raises(ValueError):
            await self._uut.query_async(["tag", " "], None, None, skip=0, take=0)
        with pytest.raises(ValueError):
            await self._uut.query_async(["tag"], None, None, skip=-1, take=0)
        with pytest.raises(ValueError):
            await self._uut.query_async(["tag"], None, None, skip=0, take=-1)

    @pytest.mark.asyncio
    async def test__only_skip_and_take_supplied__query_async__performs_query(self):
        total_count = 4
        path1 = "tag1"
        path2 = "tag2"
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(
                [
                    {
                        "totalCount": total_count,
                        "tags": [{"type": "BOOLEAN", "path": path1}],
                    },
                    {
                        "totalCount": total_count,
                        "tags": [{"type": "DATE_TIME", "path": path2}],
                    },
                ]
            )
        )

        result = await self._uut.query_async(skip=2, take=1)

        assert total_count == result.total_count
        assert result.current_page is not None
        assert 1 == len(result.current_page)
        assert path1 == result.current_page[0].path
        assert tbase.DataType.BOOLEAN == result.current_page[0].data_type
        self._client.all_requests.assert_called_once_with(
            "GET", "/nitag/v2/tags", params={"skip": "2", "take": "1"}
        )

        await result.move_next_page_async()

        assert result.current_page is not None
        assert 1 == len(result.current_page)
        assert path2 == result.current_page[0].path
        assert tbase.DataType.DATE_TIME == result.current_page[0].data_type
        assert self._client.all_requests.call_args_list == [
            mock.call("GET", "/nitag/v2/tags", params={"skip": "2", "take": "1"}),
            mock.call("GET", "/nitag/v2/tags", params={"skip": "3", "take": "1"}),
        ]

        await result.move_next_page_async()

        assert result.current_page is None

    @pytest.mark.asyncio
    async def test__only_paths_supplied__query_async__performs_query(self):
        total_count = 0
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request([{"totalCount": 0, "tags": []}])
        )

        result = await self._uut.query_async(["tag1", "tag2"])

        assert total_count == result.total_count
        self._client.all_requests.assert_called_once_with(
            "GET", "/nitag/v2/tags", params={"path": "tag1,tag2", "skip": "0"}
        )

    @pytest.mark.asyncio
    async def test__path_with_skip_and_take_supplied__query_async__performs_query(self):
        total_count = 4
        path1 = "tag1"
        path2 = "tag2"
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(
                [
                    {
                        "totalCount": total_count,
                        "tags": [{"type": "BOOLEAN", "path": path1}],
                    },
                    {
                        "totalCount": total_count,
                        "tags": [{"type": "DATE_TIME", "path": path2}],
                    },
                ]
            )
        )

        result = await self._uut.query_async(
            ["missing1", path1, "missing2", path2, "missing3"], skip=2, take=1
        )

        assert total_count == result.total_count
        assert result.current_page is not None
        assert 1 == len(result.current_page)
        assert path1 == result.current_page[0].path
        assert tbase.DataType.BOOLEAN == result.current_page[0].data_type
        paths = ",".join(("missing1", path1, "missing2", path2, "missing3"))
        self._client.all_requests.assert_called_once_with(
            "GET", "/nitag/v2/tags", params={"path": paths, "skip": "2", "take": "1"}
        )

        await result.move_next_page_async()

        assert result.current_page is not None
        assert 1 == len(result.current_page)
        assert path2 == result.current_page[0].path
        assert tbase.DataType.DATE_TIME == result.current_page[0].data_type
        assert self._client.all_requests.call_args_list == [
            mock.call(
                "GET",
                "/nitag/v2/tags",
                params={"path": paths, "skip": "2", "take": "1"},
            ),
            mock.call(
                "GET",
                "/nitag/v2/tags",
                params={"path": paths, "skip": "3", "take": "1"},
            ),
        ]

        await result.move_next_page_async()

        assert result.current_page is None

    @pytest.mark.asyncio
    async def test__paths_with_keywords_and_properties_supplied__query_async__performs_query(
        self,
    ):
        total_count = 0
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(
                [{"totalCount": total_count, "tags": []}]
            )
        )

        result = await self._uut.query_async(
            ["tag1", "tag2"],
            ["keyword1", "keyword2"],
            OrderedDict((("prop1", "value1"), ("prop2", "value2"))),
        )

        assert total_count == result.total_count
        self._client.all_requests.assert_called_once_with(
            "GET",
            "/nitag/v2/tags",
            params={
                "path": "tag1,tag2",
                "keywords": "keyword1,keyword2",
                "properties": "prop1=value1,prop2=value2",
                "skip": "0",
            },
        )

    @pytest.mark.asyncio
    async def test__only_keywords_and_properties_supplied__query_async__performs_query(
        self,
    ):
        total_count = 0
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(
                [{"totalCount": total_count, "tags": []}]
            )
        )

        result = await self._uut.query_async(
            None,
            ["keyword1", "keyword2"],
            OrderedDict((("prop1", "value1"), ("prop2", "value2"))),
        )

        assert total_count == result.total_count
        self._client.all_requests.assert_called_once_with(
            "GET",
            "/nitag/v2/tags",
            params={
                "keywords": "keyword1,keyword2",
                "properties": "prop1=value1,prop2=value2",
                "skip": "0",
            },
        )

    @pytest.mark.asyncio
    async def test__all_inputs_supplied__query_async__performs_query(self):
        total_count = 4
        path1 = "tag1"
        path2 = "tag2"
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(
                [
                    {
                        "totalCount": total_count,
                        "tags": [{"type": "BOOLEAN", "path": path1}],
                    },
                    {
                        "totalCount": total_count,
                        "tags": [{"type": "DATE_TIME", "path": path2}],
                    },
                ]
            )
        )

        result = await self._uut.query_async(
            ["missing1", path1, "missing2", path2, "missing3"],
            ["keyword1", "keyword2"],
            OrderedDict((("prop1", "value1"), ("prop2", "value2"))),
            skip=2,
            take=1,
        )

        assert total_count == result.total_count
        assert result.current_page is not None
        assert 1 == len(result.current_page)
        assert path1 == result.current_page[0].path
        assert tbase.DataType.BOOLEAN == result.current_page[0].data_type
        paths = ",".join(("missing1", path1, "missing2", path2, "missing3"))
        self._client.all_requests.assert_called_once_with(
            "GET",
            "/nitag/v2/tags",
            params={
                "path": paths,
                "keywords": "keyword1,keyword2",
                "properties": "prop1=value1,prop2=value2",
                "skip": "2",
                "take": "1",
            },
        )

        await result.move_next_page_async()

        assert result.current_page is not None
        assert 1 == len(result.current_page)
        assert path2 == result.current_page[0].path
        assert tbase.DataType.DATE_TIME == result.current_page[0].data_type
        assert self._client.all_requests.call_args_list == [
            mock.call(
                "GET",
                "/nitag/v2/tags",
                params={
                    "path": paths,
                    "keywords": "keyword1,keyword2",
                    "properties": "prop1=value1,prop2=value2",
                    "skip": "2",
                    "take": "1",
                },
            ),
            mock.call(
                "GET",
                "/nitag/v2/tags",
                params={
                    "path": paths,
                    "keywords": "keyword1,keyword2",
                    "properties": "prop1=value1,prop2=value2",
                    "skip": "3",
                    "take": "1",
                },
            ),
        ]

        await result.move_next_page_async()

        assert result.current_page is None

    def test__bad_arguments__update_with_tags__raises(self):
        valid_tag = tbase.TagData("tag", tbase.DataType.BOOLEAN)
        with pytest.raises(ValueError):
            self._uut.update(None)
        with pytest.raises(ValueError):
            self._uut.update([])
        with pytest.raises(ValueError):
            self._uut.update([valid_tag, None])
        with pytest.raises(ValueError):
            self._uut.update([valid_tag, tbase.TagData(None, tbase.DataType.BOOLEAN)])
        with pytest.raises(ValueError):
            self._uut.update([valid_tag, tbase.TagData("", tbase.DataType.BOOLEAN)])
        with pytest.raises(ValueError):
            self._uut.update([valid_tag, tbase.TagData(" ", tbase.DataType.BOOLEAN)])
        with pytest.raises(ValueError):
            self._uut.update([valid_tag, tbase.TagData("tag2", tbase.DataType.UNKNOWN)])

    def test__update_with_tags__metadata_sent_to_server(self):
        path1 = "tag1"
        path2 = "tag2"
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request([None])
        )
        keywords = ["keyword1", "keyword2"]
        properties = {"prop1": "value1", "prop2": "value2"}
        tag1 = tbase.TagData(path1, tbase.DataType.BOOLEAN, keywords, properties)
        tag1.set_retention_days(1)
        tag2 = tbase.TagData(path2, tbase.DataType.STRING)
        tag2.collect_aggregates = True
        all_properties1 = dict(properties)
        tag1._copy_retention_properties(all_properties1)
        all_properties2 = {}
        tag2._copy_retention_properties(all_properties2)

        self._uut.update([tag1, tag2])

        self._client.all_requests.assert_called_once_with(
            "POST",
            "/nitag/v2/update-tags",
            params=None,
            data={
                "tags": [
                    {
                        "path": path1,
                        "type": "BOOLEAN",
                        "keywords": keywords,
                        "properties": all_properties1,
                        "collectAggregates": False,
                    },
                    {
                        "path": path2,
                        "type": "STRING",
                        "properties": all_properties2,
                        "collectAggregates": True,
                    },
                ],
                "merge": False,
            },
        )

    def test__partial_success__update_with_tags__raises(self):
        path = "invalid"
        error = core.ApiError(
            name="Tag.OneOrMoreErrorsOccurred",
            message="One or more errors occurred",
            inner_errors=[
                core.ApiError(
                    name="Tag.InvalidDataType",
                    message="Invalid data type",
                    resource_type="tag",
                    resource_id=path,
                ),
                core.ApiError(
                    name="Tag.Conflict",
                    message="Conflict of some sort",
                    resource_type="tag",
                    resource_id="another",
                ),
            ],
        )
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(
                [
                    {
                        "error": {
                            "name": error.name,
                            "message": error.message,
                            "innerErrors": [
                                {
                                    "name": error.inner_errors[0].name,
                                    "message": error.inner_errors[0].message,
                                    "resourceType": error.inner_errors[0].resource_type,
                                    "resourceId": error.inner_errors[0].resource_id,
                                },
                                {
                                    "name": error.inner_errors[1].name,
                                    "message": error.inner_errors[1].message,
                                    "resourceType": error.inner_errors[1].resource_type,
                                    "resourceId": error.inner_errors[1].resource_id,
                                },
                            ],
                        }
                    }
                ]
            )
        )

        with pytest.raises(core.ApiException) as ex:
            self._uut.update([tbase.TagData(path, tbase.DataType.BOOLEAN)])
        assert error == ex.value.error

    def test__bad_arguments__update_with_tag_updates__raises(self):
        validUpdate = tbase.TagDataUpdate.from_tagdata(
            tbase.TagData("tag", tbase.DataType.BOOLEAN), tbase.TagUpdateFields.ALL
        )
        with pytest.raises(ValueError):
            self._uut.update(None)
        with pytest.raises(ValueError):
            self._uut.update([])
        with pytest.raises(ValueError):
            self._uut.update([validUpdate, None])

        with pytest.raises(ValueError):
            self._uut.update(
                [
                    validUpdate,
                    tbase.TagDataUpdate.from_tagdata(
                        tbase.TagData(None, tbase.DataType.BOOLEAN),
                        tbase.TagUpdateFields.ALL,
                    ),
                ]
            )

        with pytest.raises(ValueError):
            self._uut.update(
                [
                    validUpdate,
                    tbase.TagDataUpdate.from_tagdata(
                        tbase.TagData("", tbase.DataType.BOOLEAN),
                        tbase.TagUpdateFields.ALL,
                    ),
                ]
            )

        with pytest.raises(ValueError):
            self._uut.update(
                [
                    validUpdate,
                    tbase.TagDataUpdate.from_tagdata(
                        tbase.TagData(" ", tbase.DataType.BOOLEAN),
                        tbase.TagUpdateFields.ALL,
                    ),
                ]
            )

        with pytest.raises(ValueError):
            self._uut.update(
                [
                    validUpdate,
                    tbase.TagDataUpdate.from_tagdata(
                        tbase.TagData("tag2", tbase.DataType.UNKNOWN),
                        tbase.TagUpdateFields.ALL,
                    ),
                ]
            )

    def test__update_with_tag_update__metadata_merge_sent_to_server(self):
        path1 = "tag1"
        path2 = "tag2"
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request([None])
        )
        keywords = ["keyword1", "keyword2"]
        properties = {"prop1": "value1", "prop2": "value2"}
        tag1 = tbase.TagData(path1, tbase.DataType.BOOLEAN, keywords, properties)
        tag1.set_retention_days(1)
        tag2 = tbase.TagData(path2, tbase.DataType.STRING)
        tag2.collect_aggregates = True
        all_properties2 = {}
        tag2._copy_retention_properties(all_properties2)

        self._uut.update(
            [
                tbase.TagDataUpdate.from_tagdata(
                    tag1, tbase.TagUpdateFields.PROPERTIES
                ),
                tbase.TagDataUpdate.from_tagdata(tag2, tbase.TagUpdateFields.ALL),
            ]
        )

        self._client.all_requests.assert_called_once_with(
            "POST",
            "/nitag/v2/update-tags",
            params=None,
            data={
                "tags": [
                    {"path": path1, "type": "BOOLEAN", "properties": properties},
                    {
                        "path": path2,
                        "type": "STRING",
                        "properties": all_properties2,
                        "collectAggregates": True,
                    },
                ],
                "merge": True,
            },
        )

    def test__partial_success__update_with_tag_updates__raises(self):
        path = "invalid"
        error = core.ApiError(
            name="Tag.OneOrMoreErrorsOccurred",
            message="One or more errors occurred",
            inner_errors=[
                core.ApiError(
                    name="Tag.InvalidDataType",
                    message="Invalid data type",
                    resource_type="tag",
                    resource_id=path,
                ),
                core.ApiError(
                    name="Tag.Conflict",
                    message="Conflict of some sort",
                    resource_type="tag",
                    resource_id="another",
                ),
            ],
        )
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(
                [
                    {
                        "error": {
                            "name": error.name,
                            "message": error.message,
                            "innerErrors": [
                                {
                                    "name": error.inner_errors[0].name,
                                    "message": error.inner_errors[0].message,
                                    "resourceType": error.inner_errors[0].resource_type,
                                    "resourceId": error.inner_errors[0].resource_id,
                                },
                                {
                                    "name": error.inner_errors[1].name,
                                    "message": error.inner_errors[1].message,
                                    "resourceType": error.inner_errors[1].resource_type,
                                    "resourceId": error.inner_errors[1].resource_id,
                                },
                            ],
                        }
                    }
                ]
            )
        )

        with pytest.raises(core.ApiException) as ex:
            self._uut.update(
                [
                    tbase.TagDataUpdate.from_tagdata(
                        tbase.TagData(path, tbase.DataType.BOOLEAN),
                        tbase.TagUpdateFields.ALL,
                    )
                ]
            )
        assert error == ex.value.error

    @pytest.mark.asyncio
    async def test__bad_arguments__update_async_with_tags__raises(self):
        valid_tag = tbase.TagData("tag", tbase.DataType.BOOLEAN)
        with pytest.raises(ValueError):
            await self._uut.update_async(None)
        with pytest.raises(ValueError):
            await self._uut.update_async([])
        with pytest.raises(ValueError):
            await self._uut.update_async([valid_tag, None])
        with pytest.raises(ValueError):
            await self._uut.update_async(
                [valid_tag, tbase.TagData(None, tbase.DataType.BOOLEAN)]
            )
        with pytest.raises(ValueError):
            await self._uut.update_async(
                [valid_tag, tbase.TagData("", tbase.DataType.BOOLEAN)]
            )
        with pytest.raises(ValueError):
            await self._uut.update_async(
                [valid_tag, tbase.TagData(" ", tbase.DataType.BOOLEAN)]
            )
        with pytest.raises(ValueError):
            await self._uut.update_async(
                [valid_tag, tbase.TagData("tag2", tbase.DataType.UNKNOWN)]
            )

    @pytest.mark.asyncio
    async def test__update_async_with_tags__metadata_sent_to_server(self):
        path1 = "tag1"
        path2 = "tag2"
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request([None])
        )
        keywords = ["keyword1", "keyword2"]
        properties = {"prop1": "value1", "prop2": "value2"}
        tag1 = tbase.TagData(path1, tbase.DataType.BOOLEAN, keywords, properties)
        tag1.set_retention_days(1)
        tag2 = tbase.TagData(path2, tbase.DataType.STRING)
        tag2.collect_aggregates = True
        all_properties1 = dict(properties)
        tag1._copy_retention_properties(all_properties1)
        all_properties2 = {}
        tag2._copy_retention_properties(all_properties2)

        await self._uut.update_async([tag1, tag2])

        self._client.all_requests.assert_called_once_with(
            "POST",
            "/nitag/v2/update-tags",
            params=None,
            data={
                "tags": [
                    {
                        "path": path1,
                        "type": "BOOLEAN",
                        "keywords": keywords,
                        "properties": all_properties1,
                        "collectAggregates": False,
                    },
                    {
                        "path": path2,
                        "type": "STRING",
                        "properties": all_properties2,
                        "collectAggregates": True,
                    },
                ],
                "merge": False,
            },
        )

    @pytest.mark.asyncio
    async def test__partial_success__update_async_with_tags__raises(self):
        path = "invalid"
        error = core.ApiError(
            name="Tag.OneOrMoreErrorsOccurred",
            message="One or more errors occurred",
            inner_errors=[
                core.ApiError(
                    name="Tag.InvalidDataType",
                    message="Invalid data type",
                    resource_type="tag",
                    resource_id=path,
                ),
                core.ApiError(
                    name="Tag.Conflict",
                    message="Conflict of some sort",
                    resource_type="tag",
                    resource_id="another",
                ),
            ],
        )
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(
                [
                    {
                        "error": {
                            "name": error.name,
                            "message": error.message,
                            "innerErrors": [
                                {
                                    "name": error.inner_errors[0].name,
                                    "message": error.inner_errors[0].message,
                                    "resourceType": error.inner_errors[0].resource_type,
                                    "resourceId": error.inner_errors[0].resource_id,
                                },
                                {
                                    "name": error.inner_errors[1].name,
                                    "message": error.inner_errors[1].message,
                                    "resourceType": error.inner_errors[1].resource_type,
                                    "resourceId": error.inner_errors[1].resource_id,
                                },
                            ],
                        }
                    }
                ]
            )
        )

        with pytest.raises(core.ApiException) as ex:
            await self._uut.update_async([tbase.TagData(path, tbase.DataType.BOOLEAN)])
        assert error == ex.value.error

    @pytest.mark.asyncio
    async def test__bad_arguments__update_async_with_tag_updates__raises(self):
        validUpdate = tbase.TagDataUpdate.from_tagdata(
            tbase.TagData("tag", tbase.DataType.BOOLEAN), tbase.TagUpdateFields.ALL
        )
        with pytest.raises(ValueError):
            await self._uut.update_async(None)
        with pytest.raises(ValueError):
            await self._uut.update_async([])
        with pytest.raises(ValueError):
            await self._uut.update_async([validUpdate, None])

        with pytest.raises(ValueError):
            await self._uut.update_async(
                [
                    validUpdate,
                    tbase.TagDataUpdate.from_tagdata(
                        tbase.TagData(None, tbase.DataType.BOOLEAN),
                        tbase.TagUpdateFields.ALL,
                    ),
                ]
            )

        with pytest.raises(ValueError):
            await self._uut.update_async(
                [
                    validUpdate,
                    tbase.TagDataUpdate.from_tagdata(
                        tbase.TagData("", tbase.DataType.BOOLEAN),
                        tbase.TagUpdateFields.ALL,
                    ),
                ]
            )

        with pytest.raises(ValueError):
            await self._uut.update_async(
                [
                    validUpdate,
                    tbase.TagDataUpdate.from_tagdata(
                        tbase.TagData(" ", tbase.DataType.BOOLEAN),
                        tbase.TagUpdateFields.ALL,
                    ),
                ]
            )

        with pytest.raises(ValueError):
            await self._uut.update_async(
                [
                    validUpdate,
                    tbase.TagDataUpdate.from_tagdata(
                        tbase.TagData("tag2", tbase.DataType.UNKNOWN),
                        tbase.TagUpdateFields.ALL,
                    ),
                ]
            )

    @pytest.mark.asyncio
    async def test__update_async_with_tag_update__metadata_merge_sent_to_server(self):
        path1 = "tag1"
        path2 = "tag2"
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request([None])
        )
        keywords = ["keyword1", "keyword2"]
        properties = {"prop1": "value1", "prop2": "value2"}
        tag1 = tbase.TagData(path1, tbase.DataType.BOOLEAN, keywords, properties)
        tag1.set_retention_days(1)
        tag2 = tbase.TagData(path2, tbase.DataType.STRING)
        tag2.collect_aggregates = True
        all_properties2 = {}
        tag2._copy_retention_properties(all_properties2)

        await self._uut.update_async(
            [
                tbase.TagDataUpdate.from_tagdata(
                    tag1, tbase.TagUpdateFields.PROPERTIES
                ),
                tbase.TagDataUpdate.from_tagdata(tag2, tbase.TagUpdateFields.ALL),
            ]
        )

        self._client.all_requests.assert_called_once_with(
            "POST",
            "/nitag/v2/update-tags",
            params=None,
            data={
                "tags": [
                    {"path": path1, "type": "BOOLEAN", "properties": properties},
                    {
                        "path": path2,
                        "type": "STRING",
                        "properties": all_properties2,
                        "collectAggregates": True,
                    },
                ],
                "merge": True,
            },
        )

    @pytest.mark.asyncio
    async def test__partial_success__update_async_with_tag_updates__raises(self):
        path = "invalid"
        error = core.ApiError(
            name="Tag.OneOrMoreErrorsOccurred",
            message="One or more errors occurred",
            inner_errors=[
                core.ApiError(
                    name="Tag.InvalidDataType",
                    message="Invalid data type",
                    resource_type="tag",
                    resource_id=path,
                ),
                core.ApiError(
                    name="Tag.Conflict",
                    message="Conflict of some sort",
                    resource_type="tag",
                    resource_id="another",
                ),
            ],
        )
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(
                [
                    {
                        "error": {
                            "name": error.name,
                            "message": error.message,
                            "innerErrors": [
                                {
                                    "name": error.inner_errors[0].name,
                                    "message": error.inner_errors[0].message,
                                    "resourceType": error.inner_errors[0].resource_type,
                                    "resourceId": error.inner_errors[0].resource_id,
                                },
                                {
                                    "name": error.inner_errors[1].name,
                                    "message": error.inner_errors[1].message,
                                    "resourceType": error.inner_errors[1].resource_type,
                                    "resourceId": error.inner_errors[1].resource_id,
                                },
                            ],
                        }
                    }
                ]
            )
        )

        with pytest.raises(core.ApiException) as ex:
            await self._uut.update_async(
                [
                    tbase.TagDataUpdate.from_tagdata(
                        tbase.TagData(path, tbase.DataType.BOOLEAN),
                        tbase.TagUpdateFields.ALL,
                    )
                ]
            )
        assert error == ex.value.error

    def test__bad_arguments__delete_tags__raises(self):
        with pytest.raises(ValueError):
            self._uut.delete(None)
        with pytest.raises(ValueError):
            self._uut.delete([tbase.TagData("tag"), None])
        with pytest.raises(ValueError):
            self._uut.delete([tbase.TagData("tag"), tbase.TagData(None)])
        with pytest.raises(ValueError):
            self._uut.delete([tbase.TagData("tag"), tbase.TagData("")])
        with pytest.raises(ValueError):
            self._uut.delete([tbase.TagData("tag"), tbase.TagData(" ")])
        with pytest.raises(ValueError):
            self._uut.delete([tbase.TagData("tag"), tbase.TagData("*")])

    def test__delete_tags__deletes_using_paths(self):
        path1 = "tag1"
        path2 = "tag2"
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request([None, None])
        )
        self._uut.delete(
            [tbase.TagData(path1, tbase.DataType.STRING), tbase.TagData(path2)]
        )

        assert self._client.all_requests.call_args_list == [
            mock.call("DELETE", "/nitag/v2/tags/{path}", params={"path": path1}),
            mock.call("DELETE", "/nitag/v2/tags/{path}", params={"path": path2}),
        ]

    def test__bad_arguments__delete_paths__raises(self):
        with pytest.raises(ValueError):
            self._uut.delete(None)
        with pytest.raises(ValueError):
            self._uut.delete(["tag", None])
        with pytest.raises(ValueError):
            self._uut.delete(["tag", ""])
        with pytest.raises(ValueError):
            self._uut.delete(["tag", " "])
        with pytest.raises(ValueError):
            self._uut.delete(["tag", "*"])

    def test__empty_list__delete_paths__api_not_called(self):
        self._uut.delete([])

        assert self._client.all_requests.call_count == 0

    def test__small_number_of_paths__delete_paths__separate_deletes_sent_to_server(
        self,
    ):
        path1 = "tag1"
        path2 = "tag2"
        path3 = "tag3"
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request([None] * 6)
        )

        self._uut.delete([path1])
        self._uut.delete([path1, path2])
        self._uut.delete([path1, path2, path3])

        assert self._client.all_requests.call_args_list == [
            mock.call("DELETE", "/nitag/v2/tags/{path}", params={"path": path1}),
            mock.call("DELETE", "/nitag/v2/tags/{path}", params={"path": path1}),
            mock.call("DELETE", "/nitag/v2/tags/{path}", params={"path": path2}),
            mock.call("DELETE", "/nitag/v2/tags/{path}", params={"path": path1}),
            mock.call("DELETE", "/nitag/v2/tags/{path}", params={"path": path2}),
            mock.call("DELETE", "/nitag/v2/tags/{path}", params={"path": path3}),
        ]

    def test__server_error_with_small_number_of_paths__delete_paths__raises_first_exception(
        self,
    ):
        path1 = "tag1"
        path2 = "tag2"
        path3 = "tag3"
        deleteException = core.ApiException("oops")
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(
                [
                    # tag1
                    deleteException,
                    # tag1, tag2
                    None,
                    deleteException,
                    # tag1, tag2, tag3
                    deleteException,
                    deleteException,
                    deleteException,
                ]
            )
        )

        with pytest.raises(core.ApiException) as ex:
            self._uut.delete([path1])
        assert deleteException is ex.value
        with pytest.raises(core.ApiException) as ex:
            self._uut.delete([path1, path2])
        assert deleteException is ex.value
        with pytest.raises(core.ApiException) as ex:
            self._uut.delete([path1, path2, path3])
        assert deleteException is ex.value

        assert self._client.all_requests.call_args_list == [
            mock.call("DELETE", "/nitag/v2/tags/{path}", params={"path": path1}),
            mock.call("DELETE", "/nitag/v2/tags/{path}", params={"path": path1}),
            mock.call("DELETE", "/nitag/v2/tags/{path}", params={"path": path2}),
            mock.call("DELETE", "/nitag/v2/tags/{path}", params={"path": path1}),
            mock.call("DELETE", "/nitag/v2/tags/{path}", params={"path": path2}),
            mock.call("DELETE", "/nitag/v2/tags/{path}", params={"path": path3}),
        ]

    def test__many_paths__delete_paths__temporary_selection_used_for_delete(self):
        token = "selection for delete"
        paths = ["tag1", "tag2", "tag3", "tag4"]

        def mock_request(method, uri, data=None, **kwargs):
            if data is not None:
                return (
                    {"id": token, "searchPaths": data.get("searchPaths")},
                    MockResponse(method, uri),
                )
            else:
                return None, MockResponse(method, uri)

        self._client.all_requests.configure_mock(side_effect=mock_request)

        self._uut.delete(paths)

        assert self._client.all_requests.call_args_list == [
            mock.call(
                "POST",
                "/nitag/v2/selections",
                params=None,
                data={"searchPaths": paths, "inactivityTimeout": 30},
            ),
            mock.call("DELETE", "/nitag/v2/selections/{id}/tags", params={"id": token}),
            mock.call("DELETE", "/nitag/v2/selections/{id}", params={"id": token}),
        ]

    def test__server_error_with_many_paths__delete_paths__raises(self):
        token = "selection for delete"
        paths = ["tag1", "tag2", "tag3", "tag4"]
        createException = core.ApiException("can't create")
        deleteException = core.ApiException("can't delete")
        self._client.all_requests.configure_mock(side_effect=createException)

        with pytest.raises(core.ApiException) as ex:
            self._uut.delete(paths)

        assert createException is ex.value

        # ===

        def mock_request(method, uri, data=None, **kwargs):
            if data is not None:
                return (
                    {"id": token, "searchPaths": data.get("searchPaths")},
                    MockResponse(method, uri),
                )
            elif method == "DELETE":
                if uri.endswith("/tags"):
                    raise deleteException
                else:
                    return None, MockResponse(method, uri)
            else:
                assert False

        self._client.all_requests.configure_mock(side_effect=mock_request)

        with pytest.raises(core.ApiException) as ex:
            self._uut.delete(paths)

        assert deleteException is ex.value
        assert self._client.all_requests.call_args_list == [
            # From the first attempt
            mock.call(
                "POST",
                "/nitag/v2/selections",
                params=None,
                data={"searchPaths": paths, "inactivityTimeout": 30},
            ),
            # From the second attempt
            mock.call(
                "POST",
                "/nitag/v2/selections",
                params=None,
                data={"searchPaths": paths, "inactivityTimeout": 30},
            ),
            mock.call("DELETE", "/nitag/v2/selections/{id}/tags", params={"id": token}),
            mock.call("DELETE", "/nitag/v2/selections/{id}", params={"id": token}),
        ]

    def test__server_error_when_deleting_temp_selection__delete_paths__error_ignored(
        self,
    ):
        token = "selection for delete"
        paths = ["tag1", "tag2", "tag3", "tag4"]

        def mock_request(method, uri, data=None, **kwargs):
            if data is not None:
                return (
                    {"id": token, "searchPaths": data.get("searchPaths")},
                    MockResponse(method, uri),
                )
            elif method == "DELETE":
                if not uri.endswith("/tags"):
                    raise core.ApiException("can't delete selection")
                else:
                    return None, MockResponse(method, uri)
            else:
                assert False

        self._client.all_requests.configure_mock(side_effect=mock_request)

        self._uut.delete(paths)

        assert self._client.all_requests.call_args_list == [
            mock.call(
                "POST",
                "/nitag/v2/selections",
                params=None,
                data={"searchPaths": paths, "inactivityTimeout": 30},
            ),
            mock.call("DELETE", "/nitag/v2/selections/{id}/tags", params={"id": token}),
            mock.call("DELETE", "/nitag/v2/selections/{id}", params={"id": token}),
        ]

    @pytest.mark.asyncio
    async def test__bad_arguments__delete_tags_async__raises(self):
        with pytest.raises(ValueError):
            await self._uut.delete_async(None)
        with pytest.raises(ValueError):
            await self._uut.delete_async([tbase.TagData("tag"), None])
        with pytest.raises(ValueError):
            await self._uut.delete_async([tbase.TagData("tag"), tbase.TagData(None)])
        with pytest.raises(ValueError):
            await self._uut.delete_async([tbase.TagData("tag"), tbase.TagData("")])
        with pytest.raises(ValueError):
            await self._uut.delete_async([tbase.TagData("tag"), tbase.TagData(" ")])
        with pytest.raises(ValueError):
            await self._uut.delete_async([tbase.TagData("tag"), tbase.TagData("*")])

    @pytest.mark.asyncio
    async def test__delete_tags_async__deletes_using_paths(self):
        path1 = "tag1"
        path2 = "tag2"
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request([None, None])
        )
        await self._uut.delete_async(
            [tbase.TagData(path1, tbase.DataType.STRING), tbase.TagData(path2)]
        )

        assert sorted(str(c) for c in self._client.all_requests.call_args_list) == [
            str(mock.call("DELETE", "/nitag/v2/tags/{path}", params={"path": path1})),
            str(mock.call("DELETE", "/nitag/v2/tags/{path}", params={"path": path2})),
        ]

    @pytest.mark.asyncio
    async def test__bad_arguments__delete_paths_async__raises(self):
        with pytest.raises(ValueError):
            await self._uut.delete_async(None)
        with pytest.raises(ValueError):
            await self._uut.delete_async(["tag", None])
        with pytest.raises(ValueError):
            await self._uut.delete_async(["tag", ""])
        with pytest.raises(ValueError):
            await self._uut.delete_async(["tag", " "])
        with pytest.raises(ValueError):
            await self._uut.delete_async(["tag", "*"])

    @pytest.mark.asyncio
    async def test__empty_list__delete_paths_async__api_not_called(self):
        await self._uut.delete_async([])

        assert self._client.all_requests.call_count == 0

    @pytest.mark.asyncio
    async def test__small_number_of_paths__delete_paths_async__separate_deletes_sent_to_server(
        self,
    ):
        path1 = "tag1"
        path2 = "tag2"
        path3 = "tag3"
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request([None] * 6)
        )

        await asyncio.gather(
            self._uut.delete_async([path1]),
            self._uut.delete_async([path1, path2]),
            self._uut.delete_async([path1, path2, path3]),
        )

        assert sorted(str(c) for c in self._client.all_requests.call_args_list) == [
            str(mock.call("DELETE", "/nitag/v2/tags/{path}", params={"path": path1})),
            str(mock.call("DELETE", "/nitag/v2/tags/{path}", params={"path": path1})),
            str(mock.call("DELETE", "/nitag/v2/tags/{path}", params={"path": path1})),
            str(mock.call("DELETE", "/nitag/v2/tags/{path}", params={"path": path2})),
            str(mock.call("DELETE", "/nitag/v2/tags/{path}", params={"path": path2})),
            str(mock.call("DELETE", "/nitag/v2/tags/{path}", params={"path": path3})),
        ]

    @pytest.mark.asyncio
    async def test__server_error_with_small_number_of_paths__delete_paths_async__raises_first_exception(
        self,
    ):
        path1 = "tag1"
        path2 = "tag2"
        path3 = "tag3"
        deleteException = core.ApiException("oops")
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(
                [
                    # tag1
                    deleteException,
                    # tag1, tag2
                    None,
                    deleteException,
                    # tag1, tag2, tag3
                    deleteException,
                    deleteException,
                    deleteException,
                ]
            )
        )

        with pytest.raises(core.ApiException) as ex:
            await self._uut.delete_async([path1])
        assert deleteException is ex.value
        with pytest.raises(core.ApiException) as ex:
            await self._uut.delete_async([path1, path2])
        assert deleteException is ex.value
        with pytest.raises(core.ApiException) as ex:
            await self._uut.delete_async([path1, path2, path3])
        assert deleteException is ex.value

        assert sorted(str(c) for c in self._client.all_requests.call_args_list) == [
            str(mock.call("DELETE", "/nitag/v2/tags/{path}", params={"path": path1})),
            str(mock.call("DELETE", "/nitag/v2/tags/{path}", params={"path": path1})),
            str(mock.call("DELETE", "/nitag/v2/tags/{path}", params={"path": path1})),
            str(mock.call("DELETE", "/nitag/v2/tags/{path}", params={"path": path2})),
            str(mock.call("DELETE", "/nitag/v2/tags/{path}", params={"path": path2})),
            str(mock.call("DELETE", "/nitag/v2/tags/{path}", params={"path": path3})),
        ]

    @pytest.mark.asyncio
    async def test__many_paths__delete_paths_async__temporary_selection_used_for_delete(
        self,
    ):
        token = "selection for delete"
        paths = ["tag1", "tag2", "tag3", "tag4"]

        def mock_request(method, uri, data=None, **kwargs):
            if data is not None:
                return (
                    {"id": token, "searchPaths": data.get("searchPaths")},
                    MockResponse(method, uri),
                )
            else:
                return None, MockResponse(method, uri)

        self._client.all_requests.configure_mock(side_effect=mock_request)

        await self._uut.delete_async(paths)

        assert self._client.all_requests.call_args_list == [
            mock.call(
                "POST",
                "/nitag/v2/selections",
                params=None,
                data={"searchPaths": paths, "inactivityTimeout": 30},
            ),
            mock.call("DELETE", "/nitag/v2/selections/{id}/tags", params={"id": token}),
            mock.call("DELETE", "/nitag/v2/selections/{id}", params={"id": token}),
        ]

    @pytest.mark.asyncio
    async def test__server_error_with_many_paths__delete_paths_async__raises(self):
        token = "selection for delete"
        paths = ["tag1", "tag2", "tag3", "tag4"]
        createException = core.ApiException("can't create")
        deleteException = core.ApiException("can't delete")
        self._client.all_requests.configure_mock(side_effect=createException)

        with pytest.raises(core.ApiException) as ex:
            await self._uut.delete_async(paths)

        assert createException is ex.value

        # ===

        def mock_request(method, uri, data=None, **kwargs):
            if data is not None:
                return (
                    {"id": token, "searchPaths": data.get("searchPaths")},
                    MockResponse(method, uri),
                )
            elif method == "DELETE":
                if uri.endswith("/tags"):
                    raise deleteException
                else:
                    return None, MockResponse(method, uri)
            else:
                assert False

        self._client.all_requests.configure_mock(side_effect=mock_request)

        with pytest.raises(core.ApiException) as ex:
            await self._uut.delete_async(paths)

        assert deleteException is ex.value
        assert self._client.all_requests.call_args_list == [
            # From the first attempt
            mock.call(
                "POST",
                "/nitag/v2/selections",
                params=None,
                data={"searchPaths": paths, "inactivityTimeout": 30},
            ),
            # From the second attempt
            mock.call(
                "POST",
                "/nitag/v2/selections",
                params=None,
                data={"searchPaths": paths, "inactivityTimeout": 30},
            ),
            mock.call("DELETE", "/nitag/v2/selections/{id}/tags", params={"id": token}),
            mock.call("DELETE", "/nitag/v2/selections/{id}", params={"id": token}),
        ]

    @pytest.mark.asyncio
    async def test__server_error_when_deleting_temp_selection__delete_paths_async__error_ignored(
        self,
    ):
        token = "selection for delete"
        paths = ["tag1", "tag2", "tag3", "tag4"]

        def mock_request(method, uri, data=None, **kwargs):
            if data is not None:
                return (
                    {"id": token, "searchPaths": data.get("searchPaths")},
                    MockResponse(method, uri),
                )
            elif method == "DELETE":
                if not uri.endswith("/tags"):
                    raise core.ApiException("can't delete selection")
                else:
                    return None, MockResponse(method, uri)
            else:
                assert False

        self._client.all_requests.configure_mock(side_effect=mock_request)

        await self._uut.delete_async(paths)

        assert self._client.all_requests.call_args_list == [
            mock.call(
                "POST",
                "/nitag/v2/selections",
                params=None,
                data={"searchPaths": paths, "inactivityTimeout": 30},
            ),
            mock.call("DELETE", "/nitag/v2/selections/{id}/tags", params={"id": token}),
            mock.call("DELETE", "/nitag/v2/selections/{id}", params={"id": token}),
        ]

    def test__bad_arguments__create_writer__raises(self):
        with pytest.raises(ValueError):
            self._uut.create_writer(buffer_size=0)
        with pytest.raises(ValueError):
            self._uut.create_writer(max_buffer_time=timedelta(0))
        with pytest.raises(ValueError):
            self._uut.create_writer(buffer_size=0, max_buffer_time=timedelta(minutes=1))
        with pytest.raises(ValueError):
            self._uut.create_writer(buffer_size=1, max_buffer_time=timedelta(0))

    def test__create_writer_with_buffer_size__sends_when_buffer_full(self):
        path = "tag"
        value1 = 1
        value2 = 2
        writer = self._uut.create_writer(buffer_size=2)
        timestamp = datetime.now()
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request([None])
        )

        writer.write(path, tbase.DataType.INT32, value1, timestamp=timestamp)
        writer.write(path, tbase.DataType.INT32, value2, timestamp=timestamp)

        utctime = (
            datetime.fromtimestamp(timestamp.timestamp(), timezone.utc)
            .isoformat()
            .replace("+00:00", "Z")
        )
        self._client.all_requests.assert_called_once_with(
            "POST",
            "/nitag/v2/update-current-values",
            params=None,
            data=[
                {
                    "path": path,
                    "updates": [
                        {
                            "value": {"type": "INT", "value": str(value1)},
                            "timestamp": utctime,
                        },
                        {
                            "value": {"type": "INT", "value": str(value2)},
                            "timestamp": utctime,
                        },
                    ],
                },
            ],
        )

    def test__create_writer_with_buffer_time__sends_when_timer_elapsed(self):
        path = "tag"
        value = 1
        buffer_ms = 50
        writer = self._uut.create_writer(
            max_buffer_time=timedelta(milliseconds=buffer_ms)
        )
        timestamp = datetime.now()
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request([None])
        )

        writer.write(path, tbase.DataType.INT32, value, timestamp=timestamp)
        self._client.all_requests.assert_not_called()

        time.sleep(buffer_ms / 1000 * 2.5)
        if self._client.all_requests.call_count == 0:
            _wait_for_call_count(self._client.all_requests, 1, timeout=5.0)

        utctime = (
            datetime.fromtimestamp(timestamp.timestamp(), timezone.utc)
            .isoformat()
            .replace("+00:00", "Z")
        )
        self._client.all_requests.assert_called_once_with(
            "POST",
            "/nitag/v2/update-current-values",
            params=None,
            data=[
                {
                    "path": path,
                    "updates": [
                        {
                            "value": {"type": "INT", "value": str(value)},
                            "timestamp": utctime,
                        }
                    ],
                }
            ],
        )

    def test__create_writer_with_buffer_size_and_timer__obeys_both_settings(self):
        path = "tag"
        value1 = 1
        value2 = 2
        value3 = 3
        writer1 = self._uut.create_writer(
            buffer_size=2, max_buffer_time=timedelta(minutes=1)
        )
        buffer_ms = 50
        writer2 = self._uut.create_writer(
            buffer_size=2, max_buffer_time=timedelta(milliseconds=buffer_ms)
        )
        timestamp = datetime.now()
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request([None, None])
        )

        writer1.write(path, tbase.DataType.INT32, value1, timestamp=timestamp)
        writer1.write(path, tbase.DataType.INT32, value2, timestamp=timestamp)
        utctime = (
            datetime.fromtimestamp(timestamp.timestamp(), timezone.utc)
            .isoformat()
            .replace("+00:00", "Z")
        )
        self._client.all_requests.assert_called_once_with(
            "POST",
            "/nitag/v2/update-current-values",
            params=None,
            data=[
                {
                    "path": path,
                    "updates": [
                        {
                            "value": {"type": "INT", "value": str(value1)},
                            "timestamp": utctime,
                        },
                        {
                            "value": {"type": "INT", "value": str(value2)},
                            "timestamp": utctime,
                        },
                    ],
                }
            ],
        )

        writer2.write(path, tbase.DataType.INT32, value3, timestamp=timestamp)
        assert 1 == self._client.all_requests.call_count  # same as before

        time.sleep(buffer_ms / 1000 * 2.5)
        if self._client.all_requests.call_count == 1:
            _wait_for_call_count(self._client.all_requests, 2, timeout=5.0)

        assert 2 == self._client.all_requests.call_count
        assert self._client.all_requests.call_args_list[1] == mock.call(
            "POST",
            "/nitag/v2/update-current-values",
            params=None,
            data=[
                {
                    "path": path,
                    "updates": [
                        {
                            "value": {"type": "INT", "value": str(value3)},
                            "timestamp": utctime,
                        }
                    ],
                }
            ],
        )

    def test__bad_arguments__read__raises(self):
        with pytest.raises(ValueError):
            self._uut.read(None, include_timestamp=True, include_aggregates=True)
        with pytest.raises(ValueError):
            self._uut.read("", include_timestamp=True, include_aggregates=True)
        with pytest.raises(ValueError):
            self._uut.read(" ", include_timestamp=True, include_aggregates=True)
        with pytest.raises(ValueError):
            self._uut.read("*", include_timestamp=True, include_aggregates=True)

    def test__read_with_timestamp_and_aggregates__retrieves_all_data_from_server(self):
        path = "test"
        value = "success"
        now = datetime.now(timezone.utc)
        utctime = now.isoformat().replace("+00:00", "Z")
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(
                [
                    {
                        "current": {
                            "value": {"type": "STRING", "value": value},
                            "timestamp": utctime,
                        },
                        "aggregates": {"count": 7},
                    }
                ]
            )
        )

        result = self._uut.read(path, include_timestamp=True, include_aggregates=True)

        self._client.all_requests.assert_called_once_with(
            "GET", "/nitag/v2/tags/{path}/values", params={"path": path}
        )
        assert result is not None
        assert path == result.path
        assert tbase.DataType.STRING == result.data_type
        assert value == result.value
        assert now == result.timestamp
        assert 7 == result.count
        assert result.max is None
        assert result.min is None
        assert result.mean is None

    def test__read_with_aggregates__allows_missing_timestamp(self):
        path = "test"
        value = 3.14
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(
                [
                    {
                        "current": {"value": {"type": "DOUBLE", "value": str(value)}},
                        "aggregates": {
                            "min": "-1.3",
                            "max": "8.9",
                            "count": 3,
                            "avg": 4.7,
                        },
                    }
                ]
            )
        )

        result = self._uut.read(path, include_timestamp=False, include_aggregates=True)

        self._client.all_requests.assert_called_once_with(
            "GET", "/nitag/v2/tags/{path}/values", params={"path": path}
        )
        assert result is not None
        assert path == result.path
        assert tbase.DataType.DOUBLE == result.data_type
        assert value == result.value
        assert result.timestamp is None
        assert -1.3 == result.min
        assert 8.9 == result.max
        assert 3 == result.count
        assert 4.7 == result.mean

    def test__read_with_timestamp__does_not_query_aggregates(self):
        path = "test"
        value = "success"
        now = datetime.now(timezone.utc)
        utctime = now.isoformat().replace("+00:00", "Z")
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(
                [
                    {
                        "current": {
                            "value": {"type": "STRING", "value": value},
                            "timestamp": utctime,
                        }
                    }
                ]
            )
        )

        result = self._uut.read(path, include_timestamp=True, include_aggregates=False)

        self._client.all_requests.assert_called_once_with(
            "GET", "/nitag/v2/tags/{path}/values/current", params={"path": path}
        )
        assert result is not None
        assert path == result.path
        assert tbase.DataType.STRING == result.data_type
        assert value == result.value
        assert now == result.timestamp
        assert result.count is None
        assert result.max is None
        assert result.min is None
        assert result.mean is None

    def test__read_without_timestamp__retrieves_minimal_data_from_server(self):
        path = "test"
        value = "success"
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(
                [{"current": {"value": {"type": "STRING", "value": value}}}]
            )
        )

        result = self._uut.read(path, include_timestamp=False, include_aggregates=False)

        self._client.all_requests.assert_called_once_with(
            "GET", "/nitag/v2/tags/{path}/values/current/value", params={"path": path}
        )
        assert result is not None
        assert path == result.path
        assert tbase.DataType.STRING == result.data_type
        assert value == result.value
        assert result.timestamp is None
        assert result.count is None
        assert result.max is None
        assert result.min is None
        assert result.mean is None

    def test__no_tag_value__read__returns_None(self):
        path = "test"
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request([None] * 4)
        )

        assert (
            self._uut.read(path, include_timestamp=True, include_aggregates=True)
            is None
        )
        assert (
            self._uut.read(path, include_timestamp=False, include_aggregates=True)
            is None
        )
        assert (
            self._uut.read(path, include_timestamp=True, include_aggregates=False)
            is None
        )
        assert (
            self._uut.read(path, include_timestamp=False, include_aggregates=False)
            is None
        )

        assert self._client.all_requests.call_args_list == [
            mock.call("GET", "/nitag/v2/tags/{path}/values", params={"path": path}),
            mock.call("GET", "/nitag/v2/tags/{path}/values", params={"path": path}),
            mock.call(
                "GET", "/nitag/v2/tags/{path}/values/current", params={"path": path}
            ),
            mock.call(
                "GET",
                "/nitag/v2/tags/{path}/values/current/value",
                params={"path": path},
            ),
        ]

    @pytest.mark.asyncio
    async def test__bad_arguments__read_async__raises(self):
        with pytest.raises(ValueError):
            await self._uut.read_async(
                None, include_timestamp=True, include_aggregates=True
            )
        with pytest.raises(ValueError):
            await self._uut.read_async(
                "", include_timestamp=True, include_aggregates=True
            )
        with pytest.raises(ValueError):
            await self._uut.read_async(
                " ", include_timestamp=True, include_aggregates=True
            )
        with pytest.raises(ValueError):
            await self._uut.read_async(
                "*", include_timestamp=True, include_aggregates=True
            )

    @pytest.mark.asyncio
    async def test__read_async_with_timestamp_and_aggregates__retrieves_all_data_from_server(
        self,
    ):
        path = "test"
        value = "success"
        now = datetime.now(timezone.utc)
        utctime = now.isoformat().replace("+00:00", "Z")
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(
                [
                    {
                        "current": {
                            "value": {"type": "STRING", "value": value},
                            "timestamp": utctime,
                        },
                        "aggregates": {"count": 7},
                    }
                ]
            )
        )

        result = await self._uut.read_async(
            path, include_timestamp=True, include_aggregates=True
        )

        self._client.all_requests.assert_called_once_with(
            "GET", "/nitag/v2/tags/{path}/values", params={"path": path}
        )
        assert result is not None
        assert path == result.path
        assert tbase.DataType.STRING == result.data_type
        assert value == result.value
        assert now == result.timestamp
        assert 7 == result.count
        assert result.max is None
        assert result.min is None
        assert result.mean is None

    @pytest.mark.asyncio
    async def test__read_async_with_aggregates__allows_missing_timestamp(self):
        path = "test"
        value = 3.14
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(
                [
                    {
                        "current": {"value": {"type": "DOUBLE", "value": value}},
                        "aggregates": {
                            "min": "-1.3",
                            "max": "8.9",
                            "count": 3,
                            "avg": 4.7,
                        },
                    }
                ]
            )
        )

        result = await self._uut.read_async(
            path, include_timestamp=False, include_aggregates=True
        )

        self._client.all_requests.assert_called_once_with(
            "GET", "/nitag/v2/tags/{path}/values", params={"path": path}
        )
        assert result is not None
        assert path == result.path
        assert tbase.DataType.DOUBLE == result.data_type
        assert value == result.value
        assert result.timestamp is None
        assert -1.3 == result.min
        assert 8.9 == result.max
        assert 3 == result.count
        assert 4.7 == result.mean

    @pytest.mark.asyncio
    async def test__read_async_with_timestamp__does_not_query_aggregates(self):
        path = "test"
        value = "success"
        now = datetime.now(timezone.utc)
        utctime = now.isoformat().replace("+00:00", "Z")
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(
                [
                    {
                        "current": {
                            "value": {"type": "STRING", "value": value},
                            "timestamp": utctime,
                        }
                    }
                ]
            )
        )

        result = await self._uut.read_async(
            path, include_timestamp=True, include_aggregates=False
        )

        self._client.all_requests.assert_called_once_with(
            "GET", "/nitag/v2/tags/{path}/values/current", params={"path": path}
        )
        assert result is not None
        assert path == result.path
        assert tbase.DataType.STRING == result.data_type
        assert value == result.value
        assert now == result.timestamp
        assert result.count is None
        assert result.max is None
        assert result.min is None
        assert result.mean is None

    @pytest.mark.asyncio
    async def test__read_async_without_timestamp__retrieves_minimal_data_from_server(
        self,
    ):
        path = "test"
        value = "success"
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request(
                [{"current": {"value": {"type": "STRING", "value": value}}}]
            )
        )

        result = await self._uut.read_async(
            path, include_timestamp=False, include_aggregates=False
        )

        self._client.all_requests.assert_called_once_with(
            "GET", "/nitag/v2/tags/{path}/values/current/value", params={"path": path}
        )
        assert result is not None
        assert path == result.path
        assert tbase.DataType.STRING == result.data_type
        assert value == result.value
        assert result.timestamp is None
        assert result.count is None
        assert result.max is None
        assert result.min is None
        assert result.mean is None

    @pytest.mark.asyncio
    async def test__no_tag_value__read_async__returns_None(self):
        path = "test"
        self._client.all_requests.configure_mock(
            side_effect=self._get_mock_request([None] * 4)
        )

        assert (
            await self._uut.read_async(
                path, include_timestamp=True, include_aggregates=True
            )
            is None
        )
        assert (
            await self._uut.read_async(
                path, include_timestamp=False, include_aggregates=True
            )
            is None
        )
        assert (
            await self._uut.read_async(
                path, include_timestamp=True, include_aggregates=False
            )
            is None
        )
        assert (
            await self._uut.read_async(
                path, include_timestamp=False, include_aggregates=False
            )
            is None
        )

        assert self._client.all_requests.call_args_list == [
            mock.call("GET", "/nitag/v2/tags/{path}/values", params={"path": path}),
            mock.call("GET", "/nitag/v2/tags/{path}/values", params={"path": path}),
            mock.call(
                "GET", "/nitag/v2/tags/{path}/values/current", params={"path": path}
            ),
            mock.call(
                "GET",
                "/nitag/v2/tags/{path}/values/current/value",
                params={"path": path},
            ),
        ]
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/tag/test_tagqueryresultcollection.py sha256=06e3eaa4f86703127e3a3473ea85fffaa43117f112479be0a3c2df6ffd9dfce1 bytes=8560 -->
## FILE: tests/tag/test_tagqueryresultcollection.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/tag/test_tagqueryresultcollection.py`
- sha256: `06e3eaa4f86703127e3a3473ea85fffaa43117f112479be0a3c2df6ffd9dfce1`
- bytes: 8560

````python
import pytest  # type: ignore
from nisystemlink.clients.core import ApiException
from nisystemlink.clients.tag import DataType, TagData, TagQueryResultCollection


class TestTagQueryResultCollectionTests:
    class MockTagQueryResultCollection(TagQueryResultCollection):
        def __init__(self, first_page, total_count, skip):
            super().__init__(first_page, total_count, skip)
            self._setup_called = False
            self._next_total_count = None
            self._next_page = []
            self._next_throw = None
            self._calls = []

        def setup(self, next_page, new_total_count=None):
            assert (
                not self._setup_called
            ), "setup called without previous call to _query_page"
            self._setup_called = True
            if isinstance(next_page, Exception):
                self._next_throw = next_page
                self._next_page = None
            else:
                self._next_page = next_page
                self._next_throw = None
            self._next_total_count = new_total_count

        def verify(self, expected_skips):
            assert expected_skips == self._calls

        def _query_page(self, skip):
            assert self._setup_called, "_query_page called without call to setup"
            self._setup_called = False
            self._calls.append(skip)

            if self._next_throw is not None:
                raise self._next_throw

            if self._next_total_count is not None:
                self._total_count = self._next_total_count

            return self._next_page

        @property
        def total_count(self):
            return self._total_count

    def test__constructed__has_first_page_of_data(self):
        data = [
            TagData("tag1", DataType.BOOLEAN),
            TagData("tag2", DataType.DATE_TIME),
            TagData("tag3", DataType.DOUBLE),
        ]

        uut = self.MockTagQueryResultCollection(data, len(data), 0)

        itr = iter(uut)
        assert data == next(itr)
        assert len(data) == uut.total_count

    def test__iterating__second_page_queried(self):
        first_page = [
            TagData("tag1", DataType.BOOLEAN),
            TagData("tag2", DataType.DATE_TIME),
        ]

        second_page = [TagData("tag3", DataType.DOUBLE)]

        uut = self.MockTagQueryResultCollection(
            first_page, len(first_page) + len(second_page), 0
        )
        uut.setup(second_page)

        itr = iter(uut)
        next(itr)
        page = next(itr)
        assert len(first_page) + len(second_page) == uut.total_count
        assert second_page == page
        uut.verify([len(first_page)])

    def test__iterating__skip_is_respected(self):
        tag1 = TagData("tag1", DataType.BOOLEAN)
        tag2 = TagData("tag2", DataType.DATE_TIME)
        tag3 = TagData("tag3", DataType.DOUBLE)
        page1 = [tag1] * 2
        page2 = [tag2] * 5
        page3 = [tag3] * 1
        initial_skip = 1
        total_count = initial_skip + len(page1) + len(page2) + len(page3)

        uut = self.MockTagQueryResultCollection(page1, total_count, initial_skip)
        itr = iter(uut)

        next(itr)
        uut.setup(page2)
        next(itr)
        uut.setup(page3)
        next(itr)

        uut.verify([initial_skip + len(page1), initial_skip + len(page1) + len(page2)])

    def test__iterating__stops_when_done(self):
        tag = TagData("tag1", DataType.BOOLEAN)
        uut = self.MockTagQueryResultCollection([tag], 1, 0)

        assert 1 == uut.total_count

        itr = iter(uut)

        page = next(itr)
        assert len(page) == 1
        assert tag is page[0]

        with pytest.raises(StopIteration):
            next(itr)

    def test__page_count_changes__iterating__stops_early(self):
        tag = TagData("tag1", DataType.BOOLEAN)
        initial_total_count = 2
        uut = self.MockTagQueryResultCollection([tag], initial_total_count, 0)
        uut.setup(None, new_total_count=1)

        itr = iter(uut)
        next(itr)
        # according to initial_total_count, there should be more data, but there's not
        # - and that should be okay, but iterating should not produce any more results
        with pytest.raises(StopIteration):
            next(itr)

        uut.verify([1])

    def test__total_count_changes__iterating__total_count_updated(self):
        tag1 = TagData("tag1", DataType.BOOLEAN)
        tag2 = TagData("tag2", DataType.DATE_TIME)
        uut = self.MockTagQueryResultCollection([tag1], 3, 0)

        itr = iter(uut)

        page = next(itr)
        assert 3 == uut.total_count
        uut.setup([tag2], new_total_count=2)

        page = next(itr)
        assert 2 == uut.total_count
        assert 1 == len(page)
        assert tag2 is page[0]
        uut.verify([1])

        with pytest.raises(StopIteration):
            next(itr)
        assert 2 == uut.total_count
        uut.verify([1])  # still only one query has happened, due to new total_count

    def test__restart_iter__page_is_queried_with_initial_skip(self):
        initial_skip = 1
        tag2 = TagData("tag2", DataType.DATE_TIME)
        uut = self.MockTagQueryResultCollection([tag2], 3, initial_skip)

        itr = iter(uut)
        next(itr)

        tag2b = TagData("tag2b", DataType.DATE_TIME)
        uut.setup([tag2b], new_total_count=2)

        itr = iter(uut)

        page = next(itr)
        assert 2 == uut.total_count
        assert 1 == len(page)
        assert tag2b is page[0]

        with pytest.raises(StopIteration):
            next(itr)

        uut.verify([initial_skip])

    def test__no_results__constructed__iteration_is_empty(self):
        uut = self.MockTagQueryResultCollection(None, 0, 0)
        assert 0 == uut.total_count

        itr = iter(uut)
        with pytest.raises(StopIteration):
            next(itr)

    def test__server_data_removed_after_query__restart_iter__query_has_no_results(self):
        tag = TagData("tag", DataType.INT32)
        uut = self.MockTagQueryResultCollection([tag], 1, 0)

        itr = iter(uut)
        next(itr)
        assert 1 == uut.total_count

        uut.setup(None, new_total_count=0)

        itr = iter(uut)
        with pytest.raises(StopIteration):
            next(itr)
        assert 0 == uut.total_count
        uut.verify([0])

    def test__server_data_added_after_empty_query__restart_iter__query_has_results(
        self,
    ):
        tags = [TagData("tag", DataType.INT32)]
        uut = self.MockTagQueryResultCollection(None, 0, 0)

        itr = iter(uut)
        with pytest.raises(StopIteration):
            next(itr)

        uut.setup(tags, new_total_count=1)

        itr = iter(uut)

        page = next(itr)
        assert 1 == uut.total_count
        assert tags == page

        with pytest.raises(StopIteration):
            next(itr)

        uut.verify([0])

    def test__server_error__iterating__client_sees_error_but_can_restart(self):
        exception_to_throw = ApiException()
        initial_tags = [TagData("tag", DataType.INT32)]
        next_page = [TagData("tag2", DataType.STRING)]
        uut = self.MockTagQueryResultCollection(initial_tags, 2, 0)

        itr = iter(uut)
        next(itr)
        uut.setup(exception_to_throw)

        with pytest.raises(ApiException):
            next(itr)

        # Try again after error -- let it work this time
        uut.setup(next_page)
        itr = iter(uut)
        page = next(itr)
        assert next_page == page

        uut.verify([1, 0])

    def test__server_error__restart_iter__client_sees_error_but_can_retry(self):
        exception_to_throw = ApiException()
        initial_tags = [TagData("tag", DataType.INT32)]
        first_page = [TagData("tag2", DataType.STRING)]
        uut = self.MockTagQueryResultCollection(initial_tags, 1, 0)

        itr = iter(uut)
        next(itr)

        uut.setup(exception_to_throw)
        itr = iter(uut)
        with pytest.raises(ApiException):
            next(itr)

        # Try again after error -- let it work this time
        uut.setup(first_page)
        itr = iter(uut)
        page = next(itr)
        assert first_page == page
        with pytest.raises(StopIteration):
            next(itr)

        uut.verify([0, 0])
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/tag/test_tagselection.py sha256=7297493e672d6db9a5e3230063b5f3613265e7c0f8bbdbf998e10c09334966a5 bytes=59641 -->
## FILE: tests/tag/test_tagselection.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/tag/test_tagselection.py`
- sha256: `7297493e672d6db9a5e3230063b5f3613265e7c0f8bbdbf998e10c09334966a5`
- bytes: 59641

````python
import datetime
from unittest import mock
from unittest.mock import Mock

import pytest  # type: ignore
from nisystemlink.clients.tag import DataType, TagData, TagSelection, TagSubscription
from nisystemlink.clients.tag._core._serialized_tag_with_aggregates import (
    SerializedTagWithAggregates,
)


class TestTagSelection:
    def test__invalid_metadata__constructed__raises(self):
        with pytest.raises(ValueError):
            self.MockTagSelection(None)

        with pytest.raises(ValueError):
            self.MockTagSelection([None])

        with pytest.raises(ValueError):
            self.MockTagSelection([TagData("")])

        with pytest.raises(ValueError):
            self.MockTagSelection([TagData("tag"), TagData("tag")])

    def test__constructed_with_metadata__paths_come_from_tags_without_query(self):
        path1 = "tag1"
        path2 = "tag2"
        path3 = "tag3"
        tags = [
            TagData(path1),
            TagData(path2, DataType.DATE_TIME),
            TagData(path3, DataType.DOUBLE),
        ]
        paths = [path1, path2, path3]
        selection = self.MockTagSelection(tags)

        assert paths == list(sorted(selection.paths))
        assert sorted(paths) == sorted(selection.metadata.keys())
        assert sorted(tags, key=(lambda t: t.path)) == sorted(
            selection.metadata.values(), key=(lambda t: t.path)
        )

    def test__constructed_with_metadata__appropriate_readers_created(self):
        path1 = "tag1"
        path2 = "tag2"
        path3 = "tag3"
        path4 = "tag4"
        path5 = "tag5"
        path6 = "tag6"
        path7 = "tag7"
        tags = [
            TagData(path1),
            TagData(path2, DataType.BOOLEAN),
            TagData(path3, DataType.DATE_TIME),
            TagData(path4, DataType.DOUBLE),
            TagData(path5, DataType.INT32),
            TagData(path6, DataType.STRING),
            TagData(path7, DataType.UINT64),
        ]
        paths = [path1, path2, path3, path4, path5, path6, path7]
        selection = self.MockTagSelection(tags)

        # The first tag has unknown data type and should not appear in the values collection.
        assert paths[1:] == list(sorted(selection.values.keys()))
        assert selection.values[path2].data_type == DataType.BOOLEAN
        assert selection.values[path3].data_type == DataType.DATE_TIME
        assert selection.values[path4].data_type == DataType.DOUBLE
        assert selection.values[path5].data_type == DataType.INT32
        assert selection.values[path6].data_type == DataType.STRING
        assert selection.values[path7].data_type == DataType.UINT64

        for key, value in selection.values.items():
            assert key == value.path

    def test__constructed_with_invalid_query_data__raises(self):
        with pytest.raises(ValueError):
            self.MockTagSelection(None, [""] * 0)

        with pytest.raises(ValueError):
            self.MockTagSelection([None])

        with pytest.raises(ValueError):
            self.MockTagSelection([TagData("")])

        with pytest.raises(ValueError):
            self.MockTagSelection([TagData("tag"), TagData("tag")])

    def test__constructed_with_metadata_and_queries__uses_given_data_without_additional_query(
        self,
    ):
        path1 = "tag1"
        path2 = "tag2"
        path3 = "tag3"
        queries = ["tag1", "tag*"]
        tags = [
            TagData(path1),
            TagData(path2, DataType.DATE_TIME),
            TagData(path3, DataType.DOUBLE),
        ]
        tag_paths = [path1, path2, path3]
        selection = self.MockTagSelection(tags, queries)

        assert sorted(queries) == sorted(selection.paths)
        assert sorted(tag_paths) == sorted(selection.metadata.keys())
        assert sorted(tags, key=(lambda t: t.path)) == sorted(
            selection.metadata.values(), key=(lambda t: t.path)
        )

    def test__constructed_with_metadata_and_queries__appropriate_readers_created(self):
        path1 = "tag1"
        path2 = "tag2"
        path3 = "tag3"
        path4 = "tag4"
        path5 = "tag5"
        path6 = "tag6"
        path7 = "tag7"
        tags = [
            TagData(path1),
            TagData(path2, DataType.BOOLEAN),
            TagData(path3, DataType.DATE_TIME),
            TagData(path4, DataType.DOUBLE),
            TagData(path5, DataType.INT32),
            TagData(path6, DataType.STRING),
            TagData(path7, DataType.UINT64),
        ]
        reader_paths = [path2, path3, path4, path5, path6, path7]
        selection = self.MockTagSelection(tags, ["tag*"])

        # The tag with an unknown data type should not appear in the values collection.
        assert reader_paths == list(sorted(selection.values.keys()))
        assert selection.values[path2].data_type == DataType.BOOLEAN
        assert selection.values[path3].data_type == DataType.DATE_TIME
        assert selection.values[path4].data_type == DataType.DOUBLE
        assert selection.values[path5].data_type == DataType.INT32
        assert selection.values[path6].data_type == DataType.STRING
        assert selection.values[path7].data_type == DataType.UINT64

        for key, value in selection.values.items():
            assert key == value.path

    def test__invalid_tags__add_tags__raises_without_making_changes(self):
        selection = self.MockTagSelection([TagData] * 0)
        with pytest.raises(ValueError):
            selection.add_tags([None])
        with pytest.raises(ValueError):
            selection.add_tags([TagData("tag"), None])
        with pytest.raises(ValueError):
            selection.add_tags([TagData("tag"), TagData("")])
        # The strict mock will assert that _on_paths_changed was never called.

    def test__add_tags__updates_paths(self):
        path1 = "tag1"
        path2 = "tag2"
        paths = [path1, path2]
        queries = ["tag*"]
        selection = self.MockTagSelection([TagData(path1)], queries)
        selection.mock_on_paths_changed.configure_mock(side_effect=None)

        selection.add_tags([TagData(path1), TagData(path2)])
        assert sorted(paths + queries) == sorted(selection.paths)
        selection.mock_on_paths_changed.assert_called_once_with()

    def test__add_tags__updates_metadata_without_overwriting(self):
        path1 = "tag1"
        path2 = "tag2"
        tag1 = TagData(path1, DataType.BOOLEAN)
        tag2 = TagData(path2, DataType.DOUBLE)
        paths = [path1, path2]
        tags = [tag1, tag2]
        selection = self.MockTagSelection([tag1], ["tag*"])

        selection.mock_on_paths_changed.configure_mock(side_effect=None)
        # path1's updated DataType should be ignored
        selection.add_tags([TagData(path1, DataType.DATE_TIME), tag2])

        assert paths == sorted(selection.metadata.keys())
        assert sorted(tags, key=(lambda t: t.path)) == sorted(
            selection.metadata.values(), key=(lambda t: t.path)
        )
        selection.mock_on_paths_changed.assert_called_once_with()

    def test__clear_tags__all_collections_emptied(self):
        selection = self.MockTagSelection([TagData("tag1", DataType.BOOLEAN)], ["tag*"])
        selection.mock_on_paths_changed.configure_mock(side_effect=None)
        selection.clear_tags()

        assert 0 == len(selection.paths)
        assert 0 == len(selection.metadata)
        assert 0 == len(selection.values)
        selection.mock_on_paths_changed.assert_called_once_with()

    def test__close_twice__close_internal_called_once(self):
        selection = self.MockTagSelection([TagData] * 0)
        selection.mock_close_internal.configure_mock(side_effect=None)
        selection.close()
        selection.close()
        selection.mock_close_internal.assert_called_once_with()

    @pytest.mark.asyncio
    async def test__close_async_twice__close_internal_async_called_once(self):
        selection = self.MockTagSelection([TagData] * 0)
        selection.mock_close_internal_async.configure_mock(side_effect=None)
        await selection.close_async()
        await selection.close_async()
        selection.mock_close_internal_async.assert_called_once_with()

    def test__create_subscription__given_interval_used_if_valid(self):
        update_interval = datetime.timedelta(seconds=60)
        mock_subscription1 = Mock(TagSubscription)
        mock_subscription2 = Mock(TagSubscription)
        selection = self.MockTagSelection([TagData] * 0)
        selection.mock_create_subscription_internal.configure_mock(
            side_effect=[mock_subscription1, mock_subscription2]
        )

        assert mock_subscription1 is selection.create_subscription()
        assert mock_subscription2 is selection.create_subscription(
            update_interval=update_interval
        )
        with pytest.raises(ValueError):
            selection.create_subscription(
                update_interval=datetime.timedelta(seconds=-1)
            )

        assert selection.mock_create_subscription_internal.call_args_list == [
            mock.call(None),
            mock.call(update_interval),
        ]

    @pytest.mark.asyncio
    async def test__create_subscription_async__given_interval_used_if_valid(self):
        update_interval = datetime.timedelta(seconds=60)
        mock_subscription1 = Mock(TagSubscription)
        mock_subscription2 = Mock(TagSubscription)
        selection = self.MockTagSelection([TagData] * 0)
        selection.mock_create_subscription_internal_async.configure_mock(
            side_effect=[mock_subscription1, mock_subscription2]
        )

        assert mock_subscription1 is await selection.create_subscription_async()
        assert mock_subscription2 is await selection.create_subscription_async(
            update_interval=update_interval
        )
        with pytest.raises(ValueError):
            await selection.create_subscription_async(
                update_interval=datetime.timedelta(seconds=-1)
            )

        assert selection.mock_create_subscription_internal_async.call_args_list == [
            mock.call(None),
            mock.call(update_interval),
        ]

    def test__delete_tags_from_server__collections_cleared_after_delete(self):
        selection = self.MockTagSelection([TagData("tag1", DataType.BOOLEAN)], ["tag*"])
        selection.mock_delete_tags_from_server_internal.configure_mock(side_effect=None)
        selection.delete_tags_from_server()

        assert 0 == len(selection.metadata)
        assert 0 == len(selection.values)
        selection.mock_delete_tags_from_server_internal.assert_called_once_with()

    def test__delete_tags_from_server__cached_values_for_deleted_tags_removed(self):
        path2 = "tag2"
        selection = self.MockTagSelection([TagData("tag1", DataType.STRING)], ["tag*"])
        selection.mock_on_paths_changed.configure_mock(side_effect=None)
        selection.mock_read_tag_values.configure_mock(
            side_effect=None,
            return_value=[
                SerializedTagWithAggregates("tag1", DataType.STRING, "value1"),
                SerializedTagWithAggregates(path2, DataType.STRING, "value2"),
            ],
        )
        selection.mock_delete_tags_from_server_internal.configure_mock(side_effect=None)

        selection.refresh_values()
        assert (
            selection.read(path2, include_timestamp=False, include_aggregates=False)
            is not None
        )
        selection.remove_tags([path2])
        selection.delete_tags_from_server()
        selection.add_tags([TagData(path2, DataType.STRING)])

        assert (
            selection.read(path2, include_timestamp=False, include_aggregates=False)
            is None
        )

    @pytest.mark.asyncio
    async def test__delete_tags_from_server_async__collections_cleared_after_asynchronous_delete(
        self,
    ):
        selection = self.MockTagSelection([TagData("tag1", DataType.BOOLEAN)], ["tag*"])
        selection.mock_delete_tags_from_server_internal_async.configure_mock(
            side_effect=None
        )
        await selection.delete_tags_from_server_async()

        assert 0 == len(selection.metadata)
        assert 0 == len(selection.values)
        selection.mock_delete_tags_from_server_internal_async.assert_called_once_with()

    @pytest.mark.asyncio
    async def test__delete_tags_from_server_async__cached_values_for_deleted_tags_removed(
        self,
    ):
        path2 = "tag2"
        selection = self.MockTagSelection([TagData("tag1", DataType.STRING)], ["tag*"])
        selection.mock_on_paths_changed.configure_mock(side_effect=None)
        selection.mock_read_tag_values.configure_mock(
            side_effect=None,
            return_value=[
                SerializedTagWithAggregates("tag1", DataType.STRING, "value1"),
                SerializedTagWithAggregates(path2, DataType.STRING, "value2"),
            ],
        )
        selection.mock_delete_tags_from_server_internal_async.configure_mock(
            side_effect=None
        )

        selection.refresh_values()
        assert (
            await selection.read_async(
                path2, include_timestamp=False, include_aggregates=False
            )
            is not None
        )
        selection.remove_tags([path2])
        await selection.delete_tags_from_server_async()
        selection.add_tags([TagData(path2, DataType.STRING)])

        assert (
            await selection.read_async(
                path2, include_timestamp=False, include_aggregates=False
            )
            is None
        )

    def test__invalid_paths__open_tags__raises(self):
        selection = self.MockTagSelection([TagData] * 0)
        with pytest.raises(ValueError):
            selection.open_tags([None])
        with pytest.raises(ValueError):
            selection.open_tags(["path1", None])
        with pytest.raises(ValueError):
            selection.open_tags(["path1", ""])

    def test__open_tags__paths_added_without_query(self):
        selection = self.MockTagSelection([TagData] * 0)
        selection.mock_on_paths_changed.configure_mock(side_effect=None)
        selection.open_tags(["tag1", "tag2"])
        assert ["tag1", "tag2"] == list(sorted(selection.paths))
        selection.mock_on_paths_changed.assert_called_once_with()

    def test__refresh__metadata_updated_and_readers_replaced_where_type_changed(self):
        path1 = "tag1"
        path2 = "tag2"
        keywords = ["keyword1", "keyword2"]
        properties = {"prop1": "value1", "prop2": "value2"}
        selection = self.MockTagSelection(
            [TagData(path1, DataType.BOOLEAN), TagData(path2, DataType.INT32)]
        )
        selection.mock_read_tag_metadata_and_values.configure_mock(
            side_effect=None,
            return_value=(
                [
                    TagData(path1, DataType.DATE_TIME),
                    TagData(path2, DataType.INT32, keywords, properties),
                ],
                [SerializedTagWithAggregates] * 0,
            ),
        )

        original_reader = selection.values.get(path1)
        assert original_reader
        assert original_reader.data_type == DataType.BOOLEAN
        original_reader = selection.values.get(path2)
        assert original_reader
        assert original_reader.data_type == DataType.INT32

        selection.refresh()

        data = selection.metadata.get(path1)
        assert data
        assert DataType.DATE_TIME == data.data_type
        new_reader = selection.values.get(path1)
        assert new_reader
        assert new_reader.data_type == DataType.DATE_TIME

        data = selection.metadata.get(path2)
        assert data
        assert DataType.INT32 == data.data_type
        assert keywords == sorted(data.keywords)
        assert sorted(properties) == sorted(data.properties)
        new_reader = selection.values.get(path2)
        assert new_reader
        assert original_reader is new_reader

    def test__refresh__metadata_and_readers_added_and_removed(self):
        removed_path = "removed"
        existing_path = "existing"
        added_path = "added"
        selection = self.MockTagSelection(
            [
                TagData(removed_path, DataType.BOOLEAN),
                TagData(existing_path, DataType.INT32),
            ]
        )
        selection.mock_read_tag_metadata_and_values.configure_mock(
            side_effect=None,
            return_value=(
                [
                    TagData(existing_path, DataType.INT32),
                    TagData(added_path, DataType.STRING),
                ],
                [SerializedTagWithAggregates] * 0,
            ),
        )

        selection.refresh()

        assert removed_path not in selection.metadata
        assert removed_path not in selection.values

        data = selection.metadata.get(existing_path)
        assert data
        assert DataType.INT32 == data.data_type
        reader = selection.values.get(existing_path)
        assert reader
        assert reader.data_type == DataType.INT32

        data = selection.metadata.get(added_path)
        assert data
        assert DataType.STRING == data.data_type
        reader = selection.values.get(added_path)
        assert reader
        assert reader.data_type == DataType.STRING

    def test__refresh__values_updated(self):
        value_path = "tag1"
        no_value_path = "tag2"
        tags = [
            TagData(value_path, DataType.INT32),
            TagData(no_value_path, DataType.DATE_TIME),
        ]
        timestamp = datetime.datetime.now(datetime.timezone.utc)
        selection = self.MockTagSelection(tags)
        selection.mock_read_tag_metadata_and_values.configure_mock(
            side_effect=None,
            return_value=(
                tags,
                [
                    SerializedTagWithAggregates(
                        value_path, DataType.INT32, "5", timestamp, 3, "4", "9", 6.0
                    )
                ],
            ),
        )

        selection.refresh()
        value = selection.read(
            value_path, include_timestamp=True, include_aggregates=True
        )

        assert value is not None
        assert DataType.INT32 == value.data_type
        assert 5 == value.value
        assert timestamp == value.timestamp
        assert 3 == value.count
        assert 4 == value.min
        assert 9 == value.max
        assert 6.0 == value.mean
        assert (
            selection.read(
                no_value_path, include_timestamp=True, include_aggregates=True
            )
            is None
        )

    @pytest.mark.asyncio
    async def test__refresh_async__metadata_updated_and_readers_replaced_when_type_changed(
        self,
    ):
        path1 = "tag1"
        path2 = "tag2"
        keywords = ["keyword1", "keyword2"]
        properties = {"prop1": "value1", "prop2": "value2"}
        selection = self.MockTagSelection(
            [TagData(path1, DataType.BOOLEAN), TagData(path2, DataType.INT32)]
        )
        selection.mock_read_tag_metadata_and_values_async.configure_mock(
            side_effect=None,
            return_value=(
                [
                    TagData(path1, DataType.DATE_TIME),
                    TagData(path2, DataType.INT32, keywords, properties),
                ],
                [SerializedTagWithAggregates] * 0,
            ),
        )

        original_reader = selection.values.get(path1)
        assert original_reader
        assert original_reader.data_type == DataType.BOOLEAN
        original_reader = selection.values.get(path2)
        assert original_reader
        assert original_reader.data_type == DataType.INT32

        await selection.refresh_async()

        data = selection.metadata.get(path1)
        assert data
        assert DataType.DATE_TIME == data.data_type
        new_reader = selection.values.get(path1)
        assert new_reader
        assert new_reader.data_type == DataType.DATE_TIME

        data = selection.metadata.get(path2)
        assert data
        assert DataType.INT32 == data.data_type
        assert keywords == sorted(data.keywords)
        assert sorted(properties) == sorted(data.properties)
        new_reader = selection.values.get(path2)
        assert new_reader
        assert original_reader is new_reader

    @pytest.mark.asyncio
    async def test__refresh_async__metadata_and_readers_added_and_removed(self):
        removed_path = "removed"
        existing_path = "existing"
        added_path = "added"
        selection = self.MockTagSelection(
            [
                TagData(removed_path, DataType.BOOLEAN),
                TagData(existing_path, DataType.INT32),
            ]
        )
        selection.mock_read_tag_metadata_and_values_async.configure_mock(
            side_effect=None,
            return_value=(
                [
                    TagData(existing_path, DataType.INT32),
                    TagData(added_path, DataType.STRING),
                ],
                [SerializedTagWithAggregates] * 0,
            ),
        )

        await selection.refresh_async()

        assert removed_path not in selection.metadata
        assert removed_path not in selection.values

        data = selection.metadata.get(existing_path)
        assert data
        assert DataType.INT32 == data.data_type
        reader = selection.values.get(existing_path)
        assert reader
        assert reader.data_type == DataType.INT32

        data = selection.metadata.get(added_path)
        assert data
        assert DataType.STRING == data.data_type
        reader = selection.values.get(added_path)
        assert reader
        assert reader.data_type == DataType.STRING

    @pytest.mark.asyncio
    async def test__refresh_async__values_updated(self):
        value_path = "tag1"
        no_value_path = "tag2"
        tags = [
            TagData(value_path, DataType.INT32),
            TagData(no_value_path, DataType.DATE_TIME),
        ]
        timestamp = datetime.datetime.now(datetime.timezone.utc)
        selection = self.MockTagSelection(tags)
        selection.mock_read_tag_metadata_and_values_async.configure_mock(
            side_effect=None,
            return_value=(
                tags,
                [
                    SerializedTagWithAggregates(
                        value_path, DataType.INT32, "5", timestamp, 3, "4", "9", 6.0
                    )
                ],
            ),
        )

        await selection.refresh_async()
        value = await selection.read_async(
            value_path, include_timestamp=True, include_aggregates=True
        )

        assert value is not None
        assert DataType.INT32 == value.data_type
        assert 5 == value.value
        assert timestamp == value.timestamp
        assert 3 == value.count
        assert 4 == value.min
        assert 9 == value.max
        assert 6.0 == value.mean
        assert (
            await selection.read_async(
                no_value_path, include_timestamp=True, include_aggregates=True
            )
            is None
        )

    def test__refresh_metadata__metadata_updated_and_readers_replaced_when_type_changed(
        self,
    ):
        path1 = "tag1"
        path2 = "tag2"
        keywords = ["keyword1", "keyword2"]
        properties = {"prop1": "value1", "prop2": "value2"}
        selection = self.MockTagSelection(
            [TagData(path1, DataType.BOOLEAN), TagData(path2, DataType.INT32)]
        )
        selection.mock_read_tag_metadata.configure_mock(
            side_effect=None,
            return_value=[
                TagData(path1, DataType.DATE_TIME),
                TagData(path2, DataType.INT32, keywords, properties),
            ],
        )

        original_reader = selection.values.get(path1)
        assert original_reader
        assert original_reader.data_type == DataType.BOOLEAN
        original_reader = selection.values.get(path2)
        assert original_reader
        assert original_reader.data_type == DataType.INT32

        selection.refresh_metadata()

        data = selection.metadata.get(path1)
        assert data
        assert DataType.DATE_TIME == data.data_type
        new_reader = selection.values.get(path1)
        assert new_reader
        assert new_reader.data_type == DataType.DATE_TIME

        data = selection.metadata.get(path2)
        assert data
        assert DataType.INT32 == data.data_type
        assert keywords == sorted(data.keywords)
        assert sorted(properties) == sorted(data.properties)
        new_reader = selection.values.get(path2)
        assert new_reader
        assert original_reader is new_reader

    def test__refresh_metadata__metadata_and_readers_added_and_removed(self):
        removed_path = "removed"
        existing_path = "existing"
        added_path = "added"
        selection = self.MockTagSelection(
            [
                TagData(removed_path, DataType.BOOLEAN),
                TagData(existing_path, DataType.INT32),
            ]
        )
        selection.mock_read_tag_metadata.configure_mock(
            side_effect=None,
            return_value=[
                TagData(existing_path, DataType.INT32),
                TagData(added_path, DataType.STRING),
            ],
        )

        selection.refresh_metadata()

        assert removed_path not in selection.metadata
        assert removed_path not in selection.values

        data = selection.metadata.get(existing_path)
        assert data
        assert DataType.INT32 == data.data_type
        reader = selection.values.get(existing_path)
        assert reader
        assert reader.data_type == DataType.INT32

        data = selection.metadata.get(added_path)
        assert data
        assert DataType.STRING == data.data_type
        reader = selection.values.get(added_path)
        assert reader
        assert reader.data_type == DataType.STRING

    def test__refresh_metadata__cached_values_for_deleted_tags_removed(self):
        path = "tag1"
        tags = [TagData(path, DataType.INT32)]
        selection = self.MockTagSelection(tags)
        selection.mock_read_tag_metadata.configure_mock(
            side_effect=[[TagData] * 0, tags]
        )
        selection.mock_read_tag_values.configure_mock(
            side_effect=None,
            return_value=[SerializedTagWithAggregates(path, DataType.INT32, "5")],
        )

        selection.refresh_values()
        selection.refresh_metadata()
        selection.refresh_metadata()

        assert (
            selection.read(path, include_timestamp=True, include_aggregates=True)
            is None
        )

    @pytest.mark.asyncio
    async def test__refresh_metadata_async__metadata_updated_and_readers_replaced_when_type_changed(
        self,
    ):
        path1 = "tag1"
        path2 = "tag2"
        keywords = ["keyword1", "keyword2"]
        properties = {"prop1": "value1", "prop2": "value2"}
        selection = self.MockTagSelection(
            [TagData(path1, DataType.BOOLEAN), TagData(path2, DataType.INT32)]
        )
        selection.mock_read_tag_metadata_async.configure_mock(
            side_effect=None,
            return_value=(
                [
                    TagData(path1, DataType.DATE_TIME),
                    TagData(path2, DataType.INT32, keywords, properties),
                ]
            ),
        )

        original_reader = selection.values.get(path1)
        assert original_reader
        assert original_reader.data_type == DataType.BOOLEAN
        original_reader = selection.values.get(path2)
        assert original_reader
        assert original_reader.data_type == DataType.INT32

        await selection.refresh_metadata_async()

        data = selection.metadata.get(path1)
        assert data
        assert DataType.DATE_TIME == data.data_type
        new_reader = selection.values.get(path1)
        assert new_reader
        assert new_reader.data_type == DataType.DATE_TIME

        data = selection.metadata.get(path2)
        assert data
        assert DataType.INT32 == data.data_type
        assert keywords == sorted(data.keywords)
        assert sorted(properties) == sorted(data.properties)
        new_reader = selection.values.get(path2)
        assert new_reader
        assert original_reader is new_reader

    @pytest.mark.asyncio
    async def test__refresh_metadata_async__metadata_and_readers_added_and_removed(
        self,
    ):
        removed_path = "removed"
        existing_path = "existing"
        added_path = "added"
        selection = self.MockTagSelection(
            [
                TagData(removed_path, DataType.BOOLEAN),
                TagData(existing_path, DataType.INT32),
            ]
        )
        selection.mock_read_tag_metadata_async.configure_mock(
            side_effect=None,
            return_value=[
                TagData(existing_path, DataType.INT32),
                TagData(added_path, DataType.STRING),
            ],
        )

        await selection.refresh_metadata_async()

        assert removed_path not in selection.metadata
        assert removed_path not in selection.values

        data = selection.metadata.get(existing_path)
        assert data
        assert DataType.INT32 == data.data_type
        reader = selection.values.get(existing_path)
        assert reader
        assert reader.data_type == DataType.INT32

        data = selection.metadata.get(added_path)
        assert data
        assert DataType.STRING == data.data_type
        reader = selection.values.get(added_path)
        assert reader
        assert reader.data_type == DataType.STRING

    @pytest.mark.asyncio
    async def test__refresh_metadata_async__cached_values_for_deleted_tags_removed(
        self,
    ):
        path = "tag1"
        tags = [TagData(path, DataType.INT32)]
        selection = self.MockTagSelection(tags)
        selection.mock_read_tag_metadata_async.configure_mock(
            side_effect=[[TagData] * 0, tags]
        )
        selection.mock_read_tag_values.configure_mock(
            side_effect=None,
            return_value=[SerializedTagWithAggregates(path, DataType.INT32, "5")],
        )

        selection.refresh_values()
        await selection.refresh_metadata_async()
        await selection.refresh_metadata_async()

        assert (
            await selection.read_async(
                path, include_timestamp=True, include_aggregates=True
            )
            is None
        )

    def test__refresh_values__values_updated(self):
        value_path = "tag1"
        no_value_path = "tag2"
        timestamp = datetime.datetime.now(datetime.timezone.utc)
        selection = self.MockTagSelection(
            [
                TagData(value_path, DataType.INT32),
                TagData(no_value_path, DataType.DATE_TIME),
            ]
        )
        selection.mock_read_tag_values.configure_mock(
            side_effect=None,
            return_value=[
                SerializedTagWithAggregates(
                    value_path, DataType.INT32, "5", timestamp, 3, "4", "9", 6.0
                )
            ],
        )

        selection.refresh_values()
        value = selection.read(
            value_path, include_timestamp=True, include_aggregates=True
        )

        assert value is not None
        assert DataType.INT32 == value.data_type
        assert 5 == value.value
        assert timestamp == value.timestamp
        assert 3 == value.count
        assert 4 == value.min
        assert 9 == value.max
        assert 6.0 == value.mean
        assert (
            selection.read(
                no_value_path, include_timestamp=True, include_aggregates=True
            )
            is None
        )

    def test__refresh_values__metadata_and_readers_updated_when_type_changes(self):
        path = "tag1"
        selection = self.MockTagSelection([TagData(path, DataType.BOOLEAN)])
        selection.mock_read_tag_values.configure_mock(
            side_effect=None,
            return_value=[SerializedTagWithAggregates(path, DataType.INT32, "5")],
        )

        original_reader = selection.values.get(path)
        assert original_reader
        assert original_reader.data_type == DataType.BOOLEAN
        selection.refresh_values()

        tag = selection.metadata.get(path)
        assert tag
        assert DataType.INT32 == tag.data_type
        new_reader = selection.values.get(path)
        assert new_reader
        assert new_reader.data_type == DataType.INT32

    def test__refresh_values__metadata_and_reader_added_for_new_tags(self):
        path = "tag1"
        selection = self.MockTagSelection([TagData] * 0)
        selection.mock_read_tag_values.configure_mock(
            side_effect=None,
            return_value=[SerializedTagWithAggregates(path, DataType.INT32, "5")],
        )

        selection.refresh_values()

        tag = selection.metadata.get(path)
        assert tag
        assert DataType.INT32 == tag.data_type
        new_reader = selection.values.get(path)
        assert new_reader
        assert new_reader.data_type == DataType.INT32

    def test__refresh_values__deleted_tags_removed_from_cache(self):
        path = "tag1"
        selection = self.MockTagSelection([TagData(path, DataType.INT32)])
        selection.mock_read_tag_values.configure_mock(
            side_effect=[
                [SerializedTagWithAggregates(path, DataType.INT32, "5")],
                [SerializedTagWithAggregates] * 0,
            ]
        )

        selection.refresh_values()
        selection.refresh_values()

        assert (
            selection.read(path, include_timestamp=True, include_aggregates=True)
            is None
        )

    @pytest.mark.asyncio
    async def test__refresh_values_async__values_updated(self):
        value_path = "tag1"
        no_value_path = "tag2"
        timestamp = datetime.datetime.now(datetime.timezone.utc)
        selection = self.MockTagSelection(
            [
                TagData(value_path, DataType.INT32),
                TagData(no_value_path, DataType.DATE_TIME),
            ]
        )
        selection.mock_read_tag_values_async.configure_mock(
            side_effect=None,
            return_value=[
                SerializedTagWithAggregates(
                    value_path, DataType.INT32, "5", timestamp, 3, "4", "9", 6.0
                )
            ],
        )

        await selection.refresh_values_async()
        value = await selection.read_async(
            value_path, include_timestamp=True, include_aggregates=True
        )

        assert value is not None
        assert DataType.INT32 == value.data_type
        assert 5 == value.value
        assert timestamp == value.timestamp
        assert 3 == value.count
        assert 4 == value.min
        assert 9 == value.max
        assert 6.0 == value.mean
        assert (
            await selection.read_async(
                no_value_path, include_timestamp=True, include_aggregates=True
            )
            is None
        )

    @pytest.mark.asyncio
    async def test__refresh_values_async__metadata_and_readers_updated_when_type_changed(
        self,
    ):
        path = "tag1"
        selection = self.MockTagSelection([TagData(path, DataType.BOOLEAN)])
        selection.mock_read_tag_values_async.configure_mock(
            side_effect=None,
            return_value=[SerializedTagWithAggregates(path, DataType.INT32, "5")],
        )

        original_reader = selection.values.get(path)
        assert original_reader
        assert original_reader.data_type == DataType.BOOLEAN

        await selection.refresh_values_async()

        tag = selection.metadata.get(path)
        assert tag
        assert DataType.INT32 == tag.data_type
        new_reader = selection.values.get(path)
        assert new_reader
        assert new_reader.data_type == DataType.INT32

    @pytest.mark.asyncio
    async def test__refresh_values_async__metadata_and_reader_added_for_new_tags(self):
        path = "tag1"
        selection = self.MockTagSelection([TagData] * 0)
        selection.mock_read_tag_values_async.configure_mock(
            side_effect=None,
            return_value=[SerializedTagWithAggregates(path, DataType.INT32, "5")],
        )

        await selection.refresh_values_async()

        tag = selection.metadata.get(path)
        assert tag
        assert DataType.INT32 == tag.data_type
        new_reader = selection.values.get(path)
        assert new_reader
        assert new_reader.data_type == DataType.INT32

    @pytest.mark.asyncio
    async def test__refresh_values_async__deleted_tags_removed_from_cache(self):
        path = "tag1"
        selection = self.MockTagSelection([TagData(path, DataType.INT32)])
        selection.mock_read_tag_values_async.configure_mock(
            side_effect=[
                [SerializedTagWithAggregates(path, DataType.INT32, "5")],
                [SerializedTagWithAggregates] * 0,
            ]
        )

        await selection.refresh_values_async()
        await selection.refresh_values_async()

        assert (
            await selection.read_async(
                path, include_timestamp=True, include_aggregates=True
            )
            is None
        )

    def test__invalid_tags__remove_tags_by_metadata__raises_without_making_changes(
        self,
    ):
        selection = self.MockTagSelection([TagData] * 0)
        with pytest.raises(ValueError):
            selection.remove_tags(None)
        with pytest.raises(ValueError):
            selection.remove_tags([TagData("tag"), None])
        with pytest.raises(ValueError):
            selection.remove_tags([TagData("tag"), TagData("")])
        # The strict mock will assert that _on_paths_changed was never called.

    def test__remove_tags_by_metadata__paths_updated(self):
        path1 = "tag1"
        path2 = "tag2"
        selection = self.MockTagSelection(
            [TagData(path1, DataType.BOOLEAN), TagData(path2, DataType.DATE_TIME)]
        )
        selection.mock_on_paths_changed.configure_mock(side_effect=None)

        selection.remove_tags([TagData(path1)])

        assert [path2] == list(selection.paths)
        selection.mock_on_paths_changed.assert_called_once_with()

    def test__invalid_paths__remove_tags_by_path__raises_without_making_changes(self):
        selection = self.MockTagSelection([TagData] * 0)
        with pytest.raises(ValueError):
            selection.remove_tags(None)
        with pytest.raises(ValueError):
            selection.remove_tags(["tag", None])
        with pytest.raises(ValueError):
            selection.remove_tags(["tag", ""])
        # The strict mock will assert that _on_paths_changed was never called.

    def test__remove_tags_by_path__paths_updated(self):
        path1 = "tag1"
        path2 = "tag2"
        selection = self.MockTagSelection(
            [TagData(path1, DataType.BOOLEAN), TagData(path2, DataType.DATE_TIME)]
        )
        selection.mock_on_paths_changed.configure_mock(side_effect=None)

        selection.remove_tags([path1])

        assert [path2] == list(selection.paths)
        selection.mock_on_paths_changed.assert_called_once_with()

    def test__reset_aggregates__reset_aggregates_internal_called(self):
        selection = self.MockTagSelection([TagData] * 0)
        selection.mock_reset_aggregates_internal.configure_mock(side_effect=None)
        selection.reset_aggregates()
        selection.mock_reset_aggregates_internal.assert_called_once_with()

    @pytest.mark.asyncio
    async def test__reset_aggregates_async__reset_aggregates_internal_called(self):
        selection = self.MockTagSelection([TagData] * 0)
        selection.mock_reset_aggregates_internal_async.configure_mock(side_effect=None)
        await selection.reset_aggregates_async()
        selection.mock_reset_aggregates_internal_async.assert_called_once_with()

    def test__close__close_internal_called(self):
        selection = self.MockTagSelection([TagData] * 0)
        selection.mock_close_internal.configure_mock(side_effect=None)

        selection.close()
        selection.mock_close_internal.assert_called_once_with()

    def test__new_selection__read__values_refreshed(self):
        value_path = "tag1"
        no_value_path = "tag2"
        timestamp = datetime.datetime.now(datetime.timezone.utc)
        selection = self.MockTagSelection(
            [
                TagData(value_path, DataType.INT32),
                TagData(no_value_path, DataType.DATE_TIME),
            ]
        )
        selection.mock_read_tag_values.configure_mock(
            side_effect=None,
            return_value=[
                SerializedTagWithAggregates(
                    value_path, DataType.INT32, "5", timestamp, 3, "4", "9", 6.0
                )
            ],
        )

        value = selection.read(
            value_path, include_timestamp=True, include_aggregates=True
        )

        assert value is not None
        assert DataType.INT32 == value.data_type
        assert 5 == value.value
        assert timestamp == value.timestamp
        assert 3 == value.count
        assert 4 == value.min
        assert 9 == value.max
        assert 6.0 == value.mean
        assert (
            selection.read(
                no_value_path, include_timestamp=True, include_aggregates=True
            )
            is None
        )
        selection.mock_read_tag_values.assert_called_once_with()

    def test__values_cached__read__cached_values_used(self):
        path = "tag1"
        selection = self.MockTagSelection([TagData(path, DataType.INT32)])
        selection.mock_read_tag_values.configure_mock(
            side_effect=None,
            return_value=[SerializedTagWithAggregates(path, DataType.INT32, "5")],
        )

        assert selection._read(
            path, include_timestamp=True, include_aggregates=True
        ) is selection._read(path, include_timestamp=True, include_aggregates=True)
        assert (
            selection._read(path, include_timestamp=True, include_aggregates=True)
            is not None
        )
        selection.mock_read_tag_values.assert_called_once_with()

    def test__tag_has_no_value__read__returns_null(self):
        path = "tag1"
        selection = self.MockTagSelection([TagData(path, DataType.INT32)])
        selection.mock_read_tag_values.configure_mock(
            side_effect=None, return_value=[SerializedTagWithAggregates] * 0
        )

        assert (
            selection.read(path, include_timestamp=True, include_aggregates=True)
            is None
        )
        selection.mock_read_tag_values.assert_called_once_with()

    def test__tags_not_in_selection__read__raises(self):
        selection = self.MockTagSelection([TagData] * 0)
        selection.mock_read_tag_values.configure_mock(
            side_effect=None, return_value=[SerializedTagWithAggregates] * 0
        )
        with pytest.raises(ValueError):
            selection.read(None, include_timestamp=True, include_aggregates=True)
        with pytest.raises(ValueError):
            selection.read("tag", include_timestamp=True, include_aggregates=True)

    @pytest.mark.asyncio
    async def test__new_selection__read_async__values_refreshed(self):
        value_path = "tag1"
        no_value_path = "tag2"
        timestamp = datetime.datetime.now(datetime.timezone.utc)
        selection = self.MockTagSelection(
            [
                TagData(value_path, DataType.INT32),
                TagData(no_value_path, DataType.DATE_TIME),
            ]
        )
        selection.mock_read_tag_values_async.configure_mock(
            side_effect=None,
            return_value=[
                SerializedTagWithAggregates(
                    value_path, DataType.INT32, "5", timestamp, 3, "4", "9", 6.0
                )
            ],
        )

        value = await selection.read_async(
            value_path, include_timestamp=True, include_aggregates=True
        )

        assert value is not None
        assert DataType.INT32 == value.data_type
        assert 5 == value.value
        assert timestamp == value.timestamp
        assert 3 == value.count
        assert 4 == value.min
        assert 9 == value.max
        assert 6.0 == value.mean
        assert (
            await selection.read_async(
                no_value_path, include_timestamp=True, include_aggregates=True
            )
            is None
        )
        selection.mock_read_tag_values_async.assert_called_once_with()

    @pytest.mark.asyncio
    async def test__values_cached__read_async__cached_values_used(self):
        path = "tag1"
        selection = self.MockTagSelection([TagData(path, DataType.INT32)])
        selection.mock_read_tag_values_async.configure_mock(
            side_effect=None,
            return_value=[SerializedTagWithAggregates(path, DataType.INT32, "5")],
        )

        assert await selection._read_async(
            path, True, True
        ) is await selection._read_async(
            path, include_timestamp=True, include_aggregates=True
        )
        assert (
            await selection._read_async(
                path, include_timestamp=True, include_aggregates=True
            )
            is not None
        )
        selection.mock_read_tag_values_async.assert_called_once_with()

    @pytest.mark.asyncio
    async def test__tag_has_no_value__read_async__returns_null(self):
        path = "tag1"
        selection = self.MockTagSelection([TagData(path, DataType.INT32)])
        selection.mock_read_tag_values_async.configure_mock(
            side_effect=None, return_value=[SerializedTagWithAggregates] * 0
        )

        assert (
            await selection.read_async(
                path, include_timestamp=True, include_aggregates=True
            )
            is None
        )
        selection.mock_read_tag_values_async.assert_called_once_with()

    @pytest.mark.asyncio
    async def test__tags_not_in_selection__read_async__raises(self):
        selection = self.MockTagSelection([TagData] * 0)
        selection.mock_read_tag_values_async.configure_mock(
            side_effect=None, return_value=[SerializedTagWithAggregates] * 0
        )
        with pytest.raises(ValueError):
            await selection.read_async(
                None, include_timestamp=True, include_aggregates=True
            )
        with pytest.raises(ValueError):
            await selection.read_async(
                "tag", include_timestamp=True, include_aggregates=True
            )

    @pytest.mark.asyncio
    async def test__after_close__method_called__raises(self):
        selection = self.MockTagSelection([TagData] * 0)
        selection.mock_close_internal.configure_mock(side_effect=None)
        selection.close()

        with pytest.raises(ReferenceError):
            selection.add_tags([TagData("tag")])
        with pytest.raises(ReferenceError):
            selection.clear_tags()
        selection.close()
        await selection.close_async()
        with pytest.raises(ReferenceError):
            selection.create_subscription()
        with pytest.raises(ReferenceError):
            selection.create_subscription(update_interval=datetime.timedelta(seconds=1))
        with pytest.raises(ReferenceError):
            await selection.create_subscription_async()
        with pytest.raises(ReferenceError):
            await selection.create_subscription_async(
                update_interval=datetime.timedelta(seconds=1)
            )
        with pytest.raises(ReferenceError):
            selection.delete_tags_from_server()
        with pytest.raises(ReferenceError):
            await selection.delete_tags_from_server_async()
        with pytest.raises(ReferenceError):
            selection.open_tags(["tag"])
        with pytest.raises(ReferenceError):
            selection.refresh()
        with pytest.raises(ReferenceError):
            await selection.refresh_async()
        with pytest.raises(ReferenceError):
            selection.refresh_metadata()
        with pytest.raises(ReferenceError):
            await selection.refresh_metadata_async()
        with pytest.raises(ReferenceError):
            selection.refresh_values()
        with pytest.raises(ReferenceError):
            await selection.refresh_values_async()
        with pytest.raises(ReferenceError):
            selection.remove_tags([TagData("tag")])
        with pytest.raises(ReferenceError):
            selection.remove_tags(["tag"])
        with pytest.raises(ReferenceError):
            selection.reset_aggregates()
        with pytest.raises(ReferenceError):
            await selection.reset_aggregates_async()
        selection.close()
        with pytest.raises(ReferenceError):
            selection.read("tag", include_timestamp=True, include_aggregates=True)
        with pytest.raises(ReferenceError):
            await selection.read_async(
                "tag", include_timestamp=True, include_aggregates=True
            )

        selection.mock_close_internal.assert_called_once_with()

    @pytest.mark.asyncio
    async def test__selection_context_exited__method_called__raises(self):
        selection = self.MockTagSelection([TagData] * 0)
        selection.mock_close_internal.configure_mock(side_effect=None)
        with selection:
            pass

        with pytest.raises(ReferenceError):
            selection.add_tags([TagData("tag")])
        with pytest.raises(ReferenceError):
            selection.clear_tags()
        selection.close()
        await selection.close_async()
        with pytest.raises(ReferenceError):
            selection.create_subscription()
        with pytest.raises(ReferenceError):
            selection.create_subscription(update_interval=datetime.timedelta(seconds=1))
        with pytest.raises(ReferenceError):
            await selection.create_subscription_async()
        with pytest.raises(ReferenceError):
            await selection.create_subscription_async(
                update_interval=datetime.timedelta(seconds=1)
            )
        with pytest.raises(ReferenceError):
            selection.delete_tags_from_server()
        with pytest.raises(ReferenceError):
            await selection.delete_tags_from_server_async()
        with pytest.raises(ReferenceError):
            selection.open_tags(["tag"])
        with pytest.raises(ReferenceError):
            selection.refresh()
        with pytest.raises(ReferenceError):
            await selection.refresh_async()
        with pytest.raises(ReferenceError):
            selection.refresh_metadata()
        with pytest.raises(ReferenceError):
            await selection.refresh_metadata_async()
        with pytest.raises(ReferenceError):
            selection.refresh_values()
        with pytest.raises(ReferenceError):
            await selection.refresh_values_async()
        with pytest.raises(ReferenceError):
            selection.remove_tags([TagData("tag")])
        with pytest.raises(ReferenceError):
            selection.remove_tags(["tag"])
        with pytest.raises(ReferenceError):
            selection.reset_aggregates()
        with pytest.raises(ReferenceError):
            await selection.reset_aggregates_async()
        selection.close()
        with pytest.raises(ReferenceError):
            selection.read("tag", include_timestamp=True, include_aggregates=True)
        with pytest.raises(ReferenceError):
            await selection.read_async(
                "tag", include_timestamp=True, include_aggregates=True
            )

        selection.mock_close_internal.assert_called_once_with()

    @pytest.mark.asyncio
    async def test__after_close_async__method_called__raises(self):
        selection = self.MockTagSelection([TagData] * 0)
        selection.mock_close_internal_async.configure_mock(side_effect=None)
        await selection.close_async()

        with pytest.raises(ReferenceError):
            selection.add_tags([TagData("tag")])
        with pytest.raises(ReferenceError):
            selection.clear_tags()
        selection.close()
        await selection.close_async()
        with pytest.raises(ReferenceError):
            selection.create_subscription()
        with pytest.raises(ReferenceError):
            selection.create_subscription(update_interval=datetime.timedelta(seconds=1))
        with pytest.raises(ReferenceError):
            await selection.create_subscription_async()
        with pytest.raises(ReferenceError):
            await selection.create_subscription_async(
                update_interval=datetime.timedelta(seconds=1)
            )
        with pytest.raises(ReferenceError):
            selection.delete_tags_from_server()
        with pytest.raises(ReferenceError):
            await selection.delete_tags_from_server_async()
        with pytest.raises(ReferenceError):
            selection.open_tags(["tag"])
        with pytest.raises(ReferenceError):
            selection.refresh()
        with pytest.raises(ReferenceError):
            await selection.refresh_async()
        with pytest.raises(ReferenceError):
            selection.refresh_metadata()
        with pytest.raises(ReferenceError):
            await selection.refresh_metadata_async()
        with pytest.raises(ReferenceError):
            selection.refresh_values()
        with pytest.raises(ReferenceError):
            await selection.refresh_values_async()
        with pytest.raises(ReferenceError):
            selection.remove_tags([TagData("tag")])
        with pytest.raises(ReferenceError):
            selection.remove_tags(["tag"])
        with pytest.raises(ReferenceError):
            selection.reset_aggregates()
        with pytest.raises(ReferenceError):
            await selection.reset_aggregates_async()
        selection.close()
        with pytest.raises(ReferenceError):
            selection.read("tag", include_timestamp=True, include_aggregates=True)
        with pytest.raises(ReferenceError):
            await selection.read_async(
                "tag", include_timestamp=True, include_aggregates=True
            )

        selection.mock_close_internal_async.assert_called_once_with()

    class MockTagSelection(TagSelection):
        def __init__(self, tags, paths=None):
            self.mock_buffer_value = Mock(side_effect=NotImplementedError)
            self.mock_close_internal = Mock(return_value=None)
            self.mock_close_internal_async = Mock(side_effect=NotImplementedError)
            self.mock_create_subscription_internal = Mock(
                side_effect=NotImplementedError
            )
            self.mock_create_subscription_internal_async = Mock(
                side_effect=NotImplementedError
            )
            self.mock_delete_tags_from_server_internal = Mock(
                side_effect=NotImplementedError
            )
            self.mock_delete_tags_from_server_internal_async = Mock(
                side_effect=NotImplementedError
            )
            self.mock_on_paths_changed = Mock(wraps=super()._on_paths_changed)
            self.mock_read_tag_metadata = Mock(side_effect=NotImplementedError)
            self.mock_read_tag_metadata_and_values = Mock(
                side_effect=NotImplementedError
            )
            self.mock_read_tag_metadata_and_values_async = Mock(
                side_effect=NotImplementedError
            )
            self.mock_read_tag_metadata_async = Mock(side_effect=NotImplementedError)
            self.mock_read_tag_values = Mock(side_effect=NotImplementedError)
            self.mock_read_tag_values_async = Mock(side_effect=NotImplementedError)
            self.mock_reset_aggregates_internal = Mock(side_effect=NotImplementedError)
            self.mock_reset_aggregates_internal_async = Mock(
                side_effect=NotImplementedError
            )

            super().__init__(tags, paths)

        def _close_internal(self, *args, **kwargs):
            return self.mock_close_internal(*args, **kwargs)

        async def _close_internal_async(self, *args, **kwargs):
            return self.mock_close_internal_async(*args, **kwargs)

        def _create_subscription_internal(self, *args, **kwargs):
            return self.mock_create_subscription_internal(*args, **kwargs)

        async def _create_subscription_internal_async(self, *args, **kwargs):
            return self.mock_create_subscription_internal_async(*args, **kwargs)

        def _delete_tags_from_server_internal(self, *args, **kwargs):
            return self.mock_delete_tags_from_server_internal(*args, **kwargs)

        async def _delete_tags_from_server_internal_async(self, *args, **kwargs):
            return self.mock_delete_tags_from_server_internal_async(*args, **kwargs)

        def _on_paths_changed(self, *args, **kwargs):
            return self.mock_on_paths_changed(*args, **kwargs)

        def _read_tag_metadata(self, *args, **kwargs):
            return self.mock_read_tag_metadata(*args, **kwargs)

        def _read_tag_metadata_and_values(self, *args, **kwargs):
            return self.mock_read_tag_metadata_and_values(*args, **kwargs)

        async def _read_tag_metadata_and_values_async(self, *args, **kwargs):
            return self.mock_read_tag_metadata_and_values_async(*args, **kwargs)

        async def _read_tag_metadata_async(self, *args, **kwargs):
            return self.mock_read_tag_metadata_async(*args, **kwargs)

        def _read_tag_values(self, *args, **kwargs):
            return self.mock_read_tag_values(*args, **kwargs)

        async def _read_tag_values_async(self, *args, **kwargs):
            return self.mock_read_tag_values_async(*args, **kwargs)

        def _reset_aggregates_internal(self, *args, **kwargs):
            return self.mock_reset_aggregates_internal(*args, **kwargs)

        async def _reset_aggregates_internal_async(self, *args, **kwargs):
            return self.mock_reset_aggregates_internal_async(*args, **kwargs)
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/test_service_package_exports.py sha256=b3ed16b244666677406a24c300148188cd7617bbb199a95c1d6d22301c47d7fa bytes=2841 -->
## FILE: tests/test_service_package_exports.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/test_service_package_exports.py`
- sha256: `b3ed16b244666677406a24c300148188cd7617bbb199a95c1d6d22301c47d7fa`
- bytes: 2841

````python
"""Validate the public surface declared by each service package."""

import ast
import unittest
from pathlib import Path

PACKAGE_EXPORTS = {
    "alarm": ["AlarmClient"],
    "artifact": ["ArtifactClient"],
    "assetmanagement": ["AssetManagementClient"],
    "dataframe": ["DataFrameClient"],
    "feeds": ["FeedsClient"],
    "file": ["FileClient"],
    "notebook": ["NotebookClient"],
    "notification": ["NotificationClient"],
    "product": ["ProductClient"],
    "spec": ["SpecClient"],
    "systems": ["SystemsClient"],
    "tag": [
        "DataType",
        "RetentionType",
        "TagData",
        "TagWithAggregates",
        "AsyncTagQueryResultCollection",
        "ITagReader",
        "ITagWriter",
        "BufferedTagWriter",
        "TagValueReader",
        "TagValueWriter",
        "TagUpdateFields",
        "TagDataUpdate",
        "TagPathUtilities",
        "TagQueryResultCollection",
        "TagSubscription",
        "TagSelection",
        "TagManager",
    ],
    "test_plan": ["TestPlanClient"],
    "testmonitor": ["TestMonitorClient"],
    "work_item": ["WorkItemClient", "WorkItemExecuteApiException"],
}


class TestServicePackageExports(unittest.TestCase):
    """Verify service package docstrings and explicit export lists."""

    def test_service_package_exports_are_explicit(self):
        """Each service package should document and declare its public exports."""
        package_root = Path(__file__).resolve().parents[1] / "nisystemlink" / "clients"

        for package_name, exported_names in PACKAGE_EXPORTS.items():
            with self.subTest(package_name=package_name):
                module_path = package_root / package_name / "__init__.py"
                module = ast.parse(module_path.read_text(encoding="utf-8"))
                imported_names = []
                declared_exports = None
                module_docstring = ast.get_docstring(module)

                self.assertIsNotNone(module_docstring)
                if module_docstring is None:
                    self.fail(f"Missing module docstring in {module_path}")
                self.assertTrue(module_docstring.startswith("Start here with "))

                for node in module.body:
                    if isinstance(node, ast.ImportFrom):
                        imported_names.extend(alias.name for alias in node.names)
                    elif isinstance(node, ast.Assign):
                        for target in node.targets:
                            if isinstance(target, ast.Name) and target.id == "__all__":
                                declared_exports = ast.literal_eval(node.value)

                self.assertEqual(declared_exports, exported_names)
                self.assertCountEqual(imported_names, exported_names)
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/test_single_item_client_convenience_methods.py sha256=a573872b1f2654bba6e4a8f87ead519143ed6e800c6ea4cea71a18de47d7538b bytes=16668 -->
## FILE: tests/test_single_item_client_convenience_methods.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/test_single_item_client_convenience_methods.py`
- sha256: `a573872b1f2654bba6e4a8f87ead519143ed6e800c6ea4cea71a18de47d7538b`
- bytes: 16668

````python
import pytest
from nisystemlink.clients.assetmanagement import AssetManagementClient
from nisystemlink.clients.assetmanagement import models as asset_models
from nisystemlink.clients.core import ApiException
from nisystemlink.clients.product import models as product_models
from nisystemlink.clients.product import ProductClient
from nisystemlink.clients.spec import models as spec_models
from nisystemlink.clients.spec import SpecClient
from nisystemlink.clients.test_plan import models as test_plan_models
from nisystemlink.clients.test_plan import TestPlanClient
from nisystemlink.clients.testmonitor import models as testmonitor_models
from nisystemlink.clients.testmonitor import TestMonitorClient
from nisystemlink.clients.work_item import models as work_item_models
from nisystemlink.clients.work_item import WorkItemClient


class TestProductClientSingleItemConvenience:
    def test__create_product__wraps_bulk_create(self):
        request = product_models.CreateProductRequest(part_number="part-number")
        created_product = product_models.Product.model_construct(id="product-id")
        captured_products = []
        client = object.__new__(ProductClient)

        def fake_create_products(products):
            captured_products.append(products)
            return product_models.CreateProductsPartialSuccess(
                products=[created_product]
            )

        setattr(client, "create_products", fake_create_products)

        response = client.create_product(request)

        assert response == created_product
        assert captured_products == [[request]]

    def test__update_product__wraps_bulk_update(self):
        request = product_models.UpdateProductRequest(id="product-id")
        updated_product = product_models.Product.model_construct(id="product-id")
        captured_calls = []
        client = object.__new__(ProductClient)

        def fake_update_products(products, replace=False):
            captured_calls.append((products, replace))
            return product_models.CreateProductsPartialSuccess(
                products=[updated_product]
            )

        setattr(client, "update_products", fake_update_products)

        response = client.update_product(request, replace=True)

        assert response == updated_product
        assert captured_calls == [([request], True)]


class TestSpecClientSingleItemConvenience:
    def test__create_spec__wraps_bulk_create(self):
        request = spec_models.CreateSpecificationsRequestObject.model_construct(
            product_id="product-id",
            spec_id="spec-id",
        )
        created_spec = spec_models.CreatedSpecification.model_construct(id="spec-id")
        captured_requests = []
        client = object.__new__(SpecClient)

        def fake_create_specs(specs):
            captured_requests.append(specs)
            return spec_models.CreateSpecificationsPartialSuccess(
                created_specs=[created_spec]
            )

        setattr(client, "create_specs", fake_create_specs)

        response = client.create_spec(request)

        assert response == created_spec
        assert captured_requests[0].specs == [request]

    def test__update_spec__wraps_bulk_update(self):
        request = spec_models.UpdateSpecificationsRequestObject.model_construct(
            id="spec-id",
            product_id="product-id",
            spec_id="spec-id",
        )
        updated_spec = spec_models.UpdatedSpecification.model_construct(id="spec-id")
        captured_requests = []
        client = object.__new__(SpecClient)

        def fake_update_specs(specs):
            captured_requests.append(specs)
            return spec_models.UpdateSpecificationsPartialSuccess(
                updated_specs=[updated_spec]
            )

        setattr(client, "update_specs", fake_update_specs)

        response = client.update_spec(request)

        assert response == updated_spec
        assert captured_requests[0].specs == [request]

    def test__update_spec__raises_on_missing_success_payload(self):
        request = spec_models.UpdateSpecificationsRequestObject.model_construct(
            id="spec-id",
            product_id="product-id",
            spec_id="spec-id",
        )
        client = object.__new__(SpecClient)

        def fake_update_specs(_specs):
            return None

        setattr(client, "update_specs", fake_update_specs)

        with pytest.raises(
            ApiException, match="Server returned no updated specs"
        ) as exc_info:
            client.update_spec(request)

        assert exc_info.value.response_data is None


class TestAssetManagementClientSingleItemConvenience:
    def test__create_asset__wraps_bulk_create(self):
        request = asset_models.CreateAssetRequest.model_construct(
            location=asset_models.AssetLocationForCreate.model_construct()
        )
        created_asset = asset_models.Asset.model_construct(id="asset-id")
        captured_assets = []
        client = object.__new__(AssetManagementClient)

        def fake_create_assets(assets):
            captured_assets.append(assets)
            return asset_models.CreateAssetsPartialSuccessResponse(
                assets=[created_asset]
            )

        setattr(client, "create_assets", fake_create_assets)

        response = client.create_asset(request)

        assert response == created_asset
        assert captured_assets == [[request]]


class TestTestPlanClientSingleItemConvenience:
    def test__create_test_plan__wraps_bulk_create(self):
        request = test_plan_models.CreateTestPlanRequest(name="test-plan")
        created_test_plan = test_plan_models.TestPlan.model_construct(id="test-plan-id")
        captured_test_plans = []
        client = object.__new__(TestPlanClient)

        def fake_create_test_plans(test_plans):
            captured_test_plans.append(test_plans)
            return test_plan_models.CreateTestPlansPartialSuccessResponse(
                created_test_plans=[created_test_plan]
            )

        setattr(client, "create_test_plans", fake_create_test_plans)

        response = client.create_test_plan(request)

        assert response == created_test_plan
        assert captured_test_plans == [[request]]

    def test__update_test_plan__wraps_bulk_update(self):
        request = test_plan_models.UpdateTestPlanRequest(id="test-plan-id")
        updated_test_plan = test_plan_models.TestPlan.model_construct(id="test-plan-id")
        captured_requests = []
        client = object.__new__(TestPlanClient)

        def fake_update_test_plans(update_request):
            captured_requests.append(update_request)
            return test_plan_models.UpdateTestPlansResponse(
                updated_test_plans=[updated_test_plan]
            )

        setattr(client, "update_test_plans", fake_update_test_plans)

        response = client.update_test_plan(request, replace=True)

        assert response == updated_test_plan
        assert captured_requests[0].test_plans == [request]
        assert captured_requests[0].replace is True

    def test__schedule_test_plan__wraps_bulk_schedule(self):
        request = test_plan_models.ScheduleTestPlanRequest(id="test-plan-id")
        scheduled_test_plan = test_plan_models.TestPlan.model_construct(
            id="test-plan-id"
        )
        captured_requests = []
        client = object.__new__(TestPlanClient)

        def fake_schedule_test_plans(schedule_request):
            captured_requests.append(schedule_request)
            return test_plan_models.ScheduleTestPlansResponse(
                scheduled_test_plans=[scheduled_test_plan]
            )

        setattr(client, "schedule_test_plans", fake_schedule_test_plans)

        response = client.schedule_test_plan(request, replace=True)

        assert response == scheduled_test_plan
        assert captured_requests[0].test_plans == [request]
        assert captured_requests[0].replace is True

    def test__create_test_plan_template__wraps_bulk_create(self):
        request = test_plan_models.CreateTestPlanTemplateRequest.model_construct(
            name="template",
            template_group="group",
        )
        created_template = test_plan_models.TestPlanTemplate.model_construct(
            id="template-id"
        )
        captured_templates = []
        client = object.__new__(TestPlanClient)

        def fake_create_test_plan_templates(test_plan_templates):
            captured_templates.append(test_plan_templates)
            return test_plan_models.CreateTestPlanTemplatePartialSuccessResponse(
                created_test_plan_templates=[created_template]
            )

        setattr(client, "create_test_plan_templates", fake_create_test_plan_templates)

        response = client.create_test_plan_template(request)

        assert response == created_template
        assert captured_templates == [[request]]


class TestWorkItemClientSingleItemConvenience:
    def test__create_work_item__wraps_bulk_create(self):
        request = work_item_models.CreateWorkItemRequest(name="work-item")
        created_work_item = work_item_models.WorkItem.model_construct(id="work-item-id")
        captured_work_items = []
        client = object.__new__(WorkItemClient)

        def fake_create_work_items(work_items):
            captured_work_items.append(work_items)
            return work_item_models.CreateWorkItemsPartialSuccessResponse(
                created_work_items=[created_work_item]
            )

        setattr(client, "create_work_items", fake_create_work_items)

        response = client.create_work_item(request)

        assert response == created_work_item
        assert captured_work_items == [[request]]

    def test__update_work_item__wraps_bulk_update(self):
        request = work_item_models.UpdateWorkItemRequest(id="work-item-id")
        updated_work_item = work_item_models.WorkItem.model_construct(id="work-item-id")
        captured_requests = []
        client = object.__new__(WorkItemClient)

        def fake_update_work_items(update_work_items):
            captured_requests.append(update_work_items)
            return work_item_models.UpdateWorkItemsPartialSuccessResponse(
                updated_work_items=[updated_work_item]
            )

        setattr(client, "update_work_items", fake_update_work_items)

        response = client.update_work_item(request, replace=True)

        assert response == updated_work_item
        assert captured_requests[0].work_items == [request]
        assert captured_requests[0].replace is True

    def test__schedule_work_item__wraps_bulk_schedule(self):
        request = work_item_models.ScheduleWorkItemRequest(id="work-item-id")
        scheduled_work_item = work_item_models.WorkItem.model_construct(
            id="work-item-id"
        )
        captured_requests = []
        client = object.__new__(WorkItemClient)

        def fake_schedule_work_items(schedule_work_items):
            captured_requests.append(schedule_work_items)
            return work_item_models.ScheduleWorkItemsPartialSuccessResponse(
                scheduled_work_items=[scheduled_work_item]
            )

        setattr(client, "schedule_work_items", fake_schedule_work_items)

        response = client.schedule_work_item(request, replace=True)

        assert response == scheduled_work_item
        assert captured_requests[0].work_items == [request]
        assert captured_requests[0].replace is True

    def test__create_work_item_template__wraps_bulk_create(self):
        request = work_item_models.CreateWorkItemTemplateRequest(
            name="template",
            template_group="group",
            type="type",
        )
        created_template = work_item_models.WorkItemTemplate.model_construct(
            id="template-id"
        )
        captured_templates = []
        client = object.__new__(WorkItemClient)

        def fake_create_work_item_templates(work_item_templates):
            captured_templates.append(work_item_templates)
            return work_item_models.CreateWorkItemTemplatesPartialSuccessResponse(
                created_work_item_templates=[created_template]
            )

        setattr(client, "create_work_item_templates", fake_create_work_item_templates)

        response = client.create_work_item_template(request)

        assert response == created_template
        assert captured_templates == [[request]]

    def test__update_work_item_template__wraps_bulk_update(self):
        request = work_item_models.UpdateWorkItemTemplateRequest(id="template-id")
        updated_template = work_item_models.WorkItemTemplate.model_construct(
            id="template-id"
        )
        captured_requests = []
        client = object.__new__(WorkItemClient)

        def fake_update_work_item_templates(update_work_item_templates):
            captured_requests.append(update_work_item_templates)
            return work_item_models.UpdateWorkItemTemplatesPartialSuccessResponse(
                updated_work_item_templates=[updated_template]
            )

        setattr(client, "update_work_item_templates", fake_update_work_item_templates)

        response = client.update_work_item_template(request, replace=True)

        assert response == updated_template
        assert captured_requests[0].work_item_templates == [request]
        assert captured_requests[0].replace is True


class TestTestMonitorClientSingleItemConvenience:
    def test__update_result__wraps_bulk_update(self):
        request = testmonitor_models.UpdateResultRequest(id="result-id")
        updated_result = testmonitor_models.Result.model_construct(id="result-id")
        captured_calls = []
        client = object.__new__(TestMonitorClient)

        def fake_update_results(results, replace=False):
            captured_calls.append((results, replace))
            return testmonitor_models.UpdateResultsPartialSuccess(
                results=[updated_result]
            )

        setattr(client, "update_results", fake_update_results)

        response = client.update_result(request, replace=True)

        assert response == updated_result
        assert captured_calls == [([request], True)]

    def test__create_step__wraps_bulk_create(self):
        request = testmonitor_models.CreateStepRequest(
            name="step",
            result_id="result-id",
            step_id="step-id",
        )
        created_step = testmonitor_models.Step.model_construct(id="step-id")
        captured_calls = []
        client = object.__new__(TestMonitorClient)

        def fake_create_steps(steps, update_result_total_time=False):
            captured_calls.append((steps, update_result_total_time))
            return testmonitor_models.CreateStepsPartialSuccess(steps=[created_step])

        setattr(client, "create_steps", fake_create_steps)

        response = client.create_step(request, update_result_total_time=True)

        assert response == created_step
        assert captured_calls == [([request], True)]

    def test__update_step__wraps_bulk_update(self):
        request = testmonitor_models.UpdateStepRequest(
            result_id="result-id",
            step_id="step-id",
        )
        updated_step = testmonitor_models.Step.model_construct(id="step-id")
        captured_calls = []
        client = object.__new__(TestMonitorClient)

        def fake_update_steps(
            steps,
            update_result_total_time=False,
            replace_keywords=False,
            replace_properties=False,
        ):
            captured_calls.append(
                (
                    steps,
                    update_result_total_time,
                    replace_keywords,
                    replace_properties,
                )
            )
            return testmonitor_models.UpdateStepsPartialSuccess(steps=[updated_step])

        setattr(client, "update_steps", fake_update_steps)

        response = client.update_step(
            request,
            update_result_total_time=True,
            replace_keywords=True,
            replace_properties=True,
        )

        assert response == updated_step
        assert captured_calls == [([request], True, True, True)]
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/testmonitor/__init__.py sha256=ad102ca15cd43bb40a6313db2a0cc2a1cf080715eaf4b75aabed7e39921f37b2 bytes=16 -->
## FILE: tests/testmonitor/__init__.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/testmonitor/__init__.py`
- sha256: `ad102ca15cd43bb40a6313db2a0cc2a1cf080715eaf4b75aabed7e39921f37b2`
- bytes: 16

````python
# flake8: noqa
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/testmonitor/test_testmonitor_client.py sha256=c11d7d79bda44442dec8ece241cbac6f97216f063e6894b259e50d2ebc855f9e bytes=3238 -->
## FILE: tests/testmonitor/test_testmonitor_client.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/testmonitor/test_testmonitor_client.py`
- sha256: `c11d7d79bda44442dec8ece241cbac6f97216f063e6894b259e50d2ebc855f9e`
- bytes: 3238

````python
"""Tests for TestMonitorClient convenience methods."""

import pytest
from nisystemlink.clients.core import ApiError, ApiException
from nisystemlink.clients.testmonitor import TestMonitorClient
from nisystemlink.clients.testmonitor.models import (
    CreateResultRequest,
    CreateResultsPartialSuccess,
    Result,
    Status,
)


class TestTestMonitorClient:
    """Test cases for TestMonitorClient convenience methods."""

    def test__create_result__returns_created_result(self):
        """Test that create_result returns the created result on success."""
        request = CreateResultRequest(
            part_number="Part Number",
            program_name="Program Name",
            status=Status.PASSED(),
        )
        created_result = Result(
            id="result-id",
            part_number=request.part_number,
            program_name=request.program_name,
            status=request.status,
        )
        captured_results = []
        client = object.__new__(TestMonitorClient)

        def fake_create_results(results):
            captured_results.append(results)
            return CreateResultsPartialSuccess(results=[created_result])

        client.create_results = fake_create_results  # type: ignore[method-assign]

        response = client.create_result(request)

        assert response == created_result
        assert captured_results == [[request]]

    def test__create_result__raises_api_exception_on_partial_failure(self):
        """Test that create_result raises with the structured error on failure."""
        request = CreateResultRequest(
            part_number="Part Number",
            program_name="Program Name",
            status=Status.PASSED(),
        )
        error = ApiError(message="Create failed")
        client = object.__new__(TestMonitorClient)

        def fake_create_results(results):
            return CreateResultsPartialSuccess(
                results=[],
                failed=results,
                error=error,
            )

        client.create_results = fake_create_results  # type: ignore[method-assign]

        with pytest.raises(ApiException) as exc_info:
            client.create_result(request)

        assert exc_info.value.error == error
        assert exc_info.value.response_data == {
            "results": [],
            "failed": [request.model_dump(mode="json", by_alias=True)],
            "error": error.model_dump(mode="json", by_alias=True),
        }

    def test__create_result__raises_on_missing_created_result(self):
        """Test that create_result rejects an unexpected empty success payload."""
        request = CreateResultRequest(
            part_number="Part Number",
            program_name="Program Name",
            status=Status.PASSED(),
        )
        client = object.__new__(TestMonitorClient)

        def fake_create_results(_results):
            return CreateResultsPartialSuccess(results=[])

        client.create_results = fake_create_results  # type: ignore[method-assign]

        with pytest.raises(ApiException, match="Server returned no created results"):
            client.create_result(request)
````

<!--NI_OSS_SOURCE repo=nisystemlink-clients-python path=tests/testmonitor/test_testmonitor_dataframe_utilities.py sha256=719c3317e2fcd32ae557142847720aebe193a8cee5de909458ce70de794ac6d8 bytes=29755 -->
## FILE: tests/testmonitor/test_testmonitor_dataframe_utilities.py

- repository: `ni/nisystemlink-clients-python`
- source_path: `tests/testmonitor/test_testmonitor_dataframe_utilities.py`
- sha256: `719c3317e2fcd32ae557142847720aebe193a8cee5de909458ce70de794ac6d8`
- bytes: 29755

````python
import datetime
import uuid
from typing import List

import pandas as pd
import pytest
from nisystemlink.clients.testmonitor.models import (
    Measurement,
    NamedValue,
    Result,
    Status,
    StatusType,
    Step,
    StepData,
)
from nisystemlink.clients.testmonitor.utilities._dataframe_utilities import (
    convert_results_to_dataframe,
    convert_steps_to_dataframe,
)


@pytest.fixture(scope="class")
def results() -> List[Result]:
    """Sample results for testing purposes."""
    results = [
        Result(
            status=Status.PASSED(),
            started_at=datetime.datetime(
                2018, 5, 7, 18, 58, 5, 219692, tzinfo=datetime.timezone.utc
            ),
            updated_at=datetime.datetime(
                2018, 5, 7, 18, 58, 5, 219692, tzinfo=datetime.timezone.utc
            ),
            program_name="My Program Name",
            id=uuid.uuid1().hex,
            system_id=uuid.uuid1().hex,
            host_name="host name",
            part_number=uuid.uuid1().hex,
            serial_number=uuid.uuid1().hex,
            total_time_in_seconds=16.76845106446358,
            keywords=["keyword1", "keyword2"],
            properties={"property1": "value1", "property2": "value2"},
            operator="sample operator",
            file_ids=[uuid.uuid1().hex, uuid.uuid1().hex],
            data_table_ids=[uuid.uuid1().hex, uuid.uuid1().hex],
            status_type_summary={StatusType.PASSED: 1, StatusType.FAILED: 0},
            workspace=uuid.uuid1().hex,
        ),
        Result(
            status=Status.FAILED(),
            started_at=datetime.datetime(
                2018, 5, 7, 18, 58, 5, 219692, tzinfo=datetime.timezone.utc
            ),
            updated_at=datetime.datetime(
                2018, 5, 7, 18, 58, 5, 219692, tzinfo=datetime.timezone.utc
            ),
            program_name="My Program Name",
            id=uuid.uuid1().hex,
            part_number=uuid.uuid1().hex,
            total_time_in_seconds=16.76845106446358,
            keywords=[],
            properties={"property3": "value3"},
            file_ids=[uuid.uuid1().hex],
            status_type_summary={StatusType.PASSED: 0, StatusType.FAILED: 1},
            workspace=uuid.uuid1().hex,
        ),
        Result(
            status=Status(status_type=StatusType.CUSTOM, status_name="custom_status"),
            started_at=datetime.datetime(
                2018, 5, 7, 18, 58, 5, 219692, tzinfo=datetime.timezone.utc
            ),
            updated_at=datetime.datetime(
                2018, 5, 7, 18, 58, 5, 219692, tzinfo=datetime.timezone.utc
            ),
            program_name="My Program Name",
            id=uuid.uuid1().hex,
            file_ids=[uuid.uuid1().hex],
            status_type_summary={StatusType.PASSED: 0, StatusType.FAILED: 1},
            workspace=uuid.uuid1().hex,
        ),
    ]

    return results


@pytest.fixture
def mock_steps_data() -> List[Step]:
    """Fixture to return a mock step data."""
    step1 = Step(
        name="MockStep1",
        step_type="StepType",
        step_id="5ffb2bf6771fa11e877838dd1",
        parent_id="5ffb2bf6771fa11e877838dd2",
        result_id="5ffb2bf6771fa11e877838dd3",
        path="Path",
        path_ids=["path_id_11", "path_id_12"],
        status=Status(status_type=StatusType.DONE, status_name="Done"),
        total_time_in_seconds=5,
        started_at=datetime.datetime(
            2023, 3, 27, 18, 39, 49, tzinfo=datetime.timezone.utc
        ),
        updated_at=datetime.datetime(
            2024, 2, 2, 14, 22, 4, 625155, tzinfo=datetime.timezone.utc
        ),
        inputs=[
            NamedValue(name="Input00", value="input_value_00"),
            NamedValue(name="Input11", value="input_value_11"),
            NamedValue(name="Input12", value="input_value_12"),
        ],
        outputs=[
            NamedValue(name="Output11", value="output_value_11"),
            NamedValue(name="Output12", value="output_value_12"),
        ],
        data_model="STDF",
        data=StepData(
            text="data1",
            parameters=[
                Measurement(
                    name="parameter_11",
                    units="A",
                    status="Passed",
                    lowLimit="6.0",
                    highLimit="21.0",
                    measurement="11.0",
                    comparisonType="GTLT",
                ),
                Measurement(additionalProp="myValue"),
            ],
        ),
        has_children=False,
        workspace="846e294a-a007-47ac-9fc2-fac07eab240f",
        keywords=["keyword11", "keyword12"],
        properties={"property11": "property11_value", "property12": "property12_value"},
    )
    step2 = Step(
        name="MockStep2",
        step_type="StepType",
        step_id="5ffb2bf6771fa11e877838dd6",
        parent_id="5ffb2bf6771fa11e877838dd7",
        result_id="5ffb2bf6771fa11e877838dd8",
        path="Path",
        path_ids=["path_id_21", "path_id_22"],
        status=Status(status_type=StatusType.CUSTOM, status_name="newstatus"),
        total_time_in_seconds=5,
        started_at=datetime.datetime(
            2023, 3, 27, 18, 39, 49, tzinfo=datetime.timezone.utc
        ),
        updated_at=datetime.datetime(
            2024, 2, 2, 14, 22, 4, 625255, tzinfo=datetime.timezone.utc
        ),
        inputs=[
            NamedValue(name="Input00", value="input_value_00"),
            NamedValue(name="Input21", value="input_value_21"),
            NamedValue(name="Input22", value="input_value_22"),
        ],
        outputs=[
            NamedValue(name="Output21", value="output_value_21"),
            NamedValue(name="Output22", value="output_value_22"),
        ],
        data_model="STDF",
        data=StepData(
            text="data2",
            parameters=[
                Measurement(
                    name="parameter_21",
                    units="A",
                    status="Passed",
                    lowLimit="6.0",
                    highLimit="21.0",
                    measurement="11.0",
                    comparisonType="GTLT",
                    additionalData="additional_data_value",
                ),
                Measurement(
                    name="parameter_22",
                    units="C",
                    status="Passed",
                    lowLimit="7.0",
                    highLimit="22.0",
                    comparisonType="GTLT",
                ),
            ],
        ),
        has_children=True,
        workspace="846e294a-a007-47ac-9fc2-fac07eab240z",
        keywords=["keyword21", "keyword22"],
        properties={"property21": "property21_value", "property22": "property22_value"},
    )
    return [step1, step2]


@pytest.fixture
def empty_steps_data() -> List:
    """Fixture to return an empty list of steps."""
    return []


@pytest.mark.unit
class TestTestmonitorDataframeUtilities:
    def test__convert_results_with_all_fields_to_dataframe__returns_whole_results_dataframe(
        self, results
    ):
        expected_results_dataframe = self.__get_expected_results_dataframe(
            results=results
        )

        results_dataframe = convert_results_to_dataframe(
            results=results, set_id_as_index=False
        )

        assert not results_dataframe.empty
        assert len(results_dataframe.columns.tolist()) == 20
        pd.testing.assert_frame_equal(
            results_dataframe, expected_results_dataframe, check_dtype=True
        )
        assert isinstance(results_dataframe["status"].iloc[0], str)
        assert results_dataframe["started_at"].dtype == "datetime64[ns, UTC]"
        assert results_dataframe["updated_at"].dtype == "datetime64[ns, UTC]"
        assert results_dataframe["file_ids"].dtype == "object"
        assert isinstance(results_dataframe["file_ids"].iloc[0], List)
        assert results_dataframe["data_table_ids"].dtype == "object"
        assert isinstance(results_dataframe["data_table_ids"].iloc[0], List)
        assert results_dataframe["keywords"].dtype == "object"
        assert isinstance(results_dataframe["keywords"].iloc[0], List)

    def test__convert_results_with_specific_fields_to_dataframe__returns_results_dataframe_with_specific_fields(
        self, results
    ):
        results = results[1:]
        results.append(
            Result(
                status=None,
                started_at=datetime.datetime(
                    2018, 5, 7, 18, 58, 5, 219692, tzinfo=datetime.timezone.utc
                ),
                updated_at=datetime.datetime(
                    2018, 5, 7, 18, 58, 5, 219692, tzinfo=datetime.timezone.utc
                ),
                program_name="My Program Name",
                id=uuid.uuid1().hex,
                file_ids=[uuid.uuid1().hex],
                status_type_summary={StatusType.PASSED: 0, StatusType.FAILED: 1},
                workspace=uuid.uuid1().hex,
            )
        )

        expected_results_dataframe = self.__get_expected_results_dataframe(
            results=results
        )

        results_dataframe = convert_results_to_dataframe(
            results=results, set_id_as_index=False
        )

        assert not results_dataframe.empty
        assert len(results_dataframe.columns.tolist()) == 13
        pd.testing.assert_frame_equal(
            results_dataframe, expected_results_dataframe, check_dtype=True
        )
        assert isinstance(results_dataframe["status"].iloc[0], str)
        assert results_dataframe["started_at"].dtype == "datetime64[ns, UTC]"
        assert results_dataframe["updated_at"].dtype == "datetime64[ns, UTC]"
        assert results_dataframe["file_ids"].dtype == "object"
        assert isinstance(results_dataframe["file_ids"].iloc[0], List)
        assert results_dataframe["keywords"].dtype == "object"
        assert isinstance(results_dataframe["keywords"].iloc[0], List)

    def test__convert_results_to_dataframe_with_id_index__returns_results_dataframe_with_id_index(
        self, results
    ):
        expected_results_dataframe = self.__get_expected_results_dataframe(
            results=results
        )
        expected_results_dataframe = expected_results_dataframe.set_index("id")

        results_dataframe = convert_results_to_dataframe(results=results)

        assert not results_dataframe.empty
        assert len(results_dataframe.columns.tolist()) == 19
        pd.testing.assert_frame_equal(
            results_dataframe, expected_results_dataframe, check_dtype=True
        )
        assert isinstance(results_dataframe["status"].iloc[0], str)
        assert results_dataframe["started_at"].dtype == "datetime64[ns, UTC]"
        assert results_dataframe["updated_at"].dtype == "datetime64[ns, UTC]"
        assert results_dataframe["file_ids"].dtype == "object"
        assert isinstance(results_dataframe["file_ids"].iloc[0], List)
        assert results_dataframe["data_table_ids"].dtype == "object"
        assert isinstance(results_dataframe["data_table_ids"].iloc[0], List)
        assert results_dataframe["keywords"].dtype == "object"
        assert isinstance(results_dataframe["keywords"].iloc[0], List)

    def test__convert_results_to_dataframe_with_no_results__returns_empty_dataframe(
        self,
    ):
        results_dataframe = convert_results_to_dataframe(results=[])

        assert isinstance(results_dataframe, pd.DataFrame)
        assert results_dataframe.empty

    def test__convert_steps_to_dataframe__with_complete_data(
        self, mock_steps_data: List[Step]
    ):
        """Test normal case with valid step data."""
        expected_data_parameters = [
            [
                {
                    "data.measurement.name": "parameter_11",
                    "data.measurement.status": "Passed",
                    "data.measurement.measurement": "11.0",
                    "data.measurement.lowLimit": "6.0",
                    "data.measurement.highLimit": "21.0",
                    "data.measurement.units": "A",
                    "data.measurement.comparisonType": "GTLT",
                }
            ],
            [
                {
                    "data.measurement.name": "parameter_21",
                    "data.measurement.status": "Passed",
                    "data.measurement.measurement": "11.0",
                    "data.measurement.lowLimit": "6.0",
                    "data.measurement.highLimit": "21.0",
                    "data.measurement.units": "A",
                    "data.measurement.comparisonType": "GTLT",
                    "data.measurement.additionalData": "additional_data_value",
                }
            ],
        ]
        expected_steps_dataframe = self.__get_expected_steps_dataframe(
            mock_steps_data, expected_data_parameters
        )

        steps_dataframe = convert_steps_to_dataframe(mock_steps_data)

        assert not steps_dataframe.empty
        assert (
            steps_dataframe.columns.to_list()
            == expected_steps_dataframe.columns.to_list()
        )

        assert steps_dataframe["updated_at"].dtype == "datetime64[ns, UTC]"
        assert steps_dataframe["started_at"].dtype == "datetime64[ns, UTC]"
        assert steps_dataframe["path_ids"].dtype == "object"
        assert isinstance(steps_dataframe["path_ids"].iloc[0], List)
        assert steps_dataframe["keywords"].dtype == "object"
        assert isinstance(steps_dataframe["keywords"].iloc[0], List)
        pd.testing.assert_frame_equal(
            steps_dataframe, expected_steps_dataframe, check_dtype=True
        )

    def test__convert_steps_to_dataframe__with_empty_data(self, empty_steps_data: List):
        """Test case when the input steps data is empty."""
        steps_dataframe = convert_steps_to_dataframe(empty_steps_data)

        assert steps_dataframe.empty

    def test__convert_steps_to_dataframe__with_missing_fields(
        self, mock_steps_data: List[Step]
    ):
        """Test case when some fields in step data are missing."""
        expected_steps_dataframe = self.__get_expected_steps_dataframe(mock_steps_data)
        steps = mock_steps_data
        for step in steps:
            step.path_ids = None
            step.data = None
            step.inputs = None
        expected_steps_dataframe = expected_steps_dataframe.drop(
            columns=[
                "path_ids",
                "data.text",
                "inputs.Input00",
                "inputs.Input11",
                "inputs.Input12",
                "inputs.Input21",
                "inputs.Input22",
            ]
        )
        expected_steps_dataframe = expected_steps_dataframe.drop_duplicates(
            subset=["step_id", "result_id"], ignore_index=True
        )
        steps_dataframe = convert_steps_to_dataframe(steps)

        assert not steps_dataframe.empty
        assert (
            steps_dataframe.columns.to_list()
            == expected_steps_dataframe.columns.to_list()
        )
        pd.testing.assert_frame_equal(
            steps_dataframe, expected_steps_dataframe, check_dtype=True
        )

    def test__convert_steps_to_dataframe_with_callback__returns_dataframe_with_valid_measurement(
        self, mock_steps_data: List[Step]
    ):
        """Test if the function returns a dataframe of steps with valid measurement."""

        def is_measurement_data_parameter(measurement: Measurement) -> bool:
            return measurement.name is not None and hasattr(
                measurement, "additionalData"
            )

        expected_data_parameters = [
            [{}],
            [
                {
                    "data.measurement.name": "parameter_21",
                    "data.measurement.status": "Passed",
                    "data.measurement.measurement": "11.0",
                    "data.measurement.lowLimit": "6.0",
                    "data.measurement.highLimit": "21.0",
                    "data.measurement.units": "A",
                    "data.measurement.comparisonType": "GTLT",
                    "data.measurement.additionalData": "additional_data_value",
                }
            ],
        ]
        expected_steps_dataframe = self.__get_expected_steps_dataframe(
            mock_steps_data, expected_data_parameters
        )

        steps_dataframe = convert_steps_to_dataframe(
            mock_steps_data, is_measurement_data_parameter
        )

        assert not steps_dataframe.empty
        assert (
            steps_dataframe.columns.to_list()
            == expected_steps_dataframe.columns.to_list()
        )
        assert steps_dataframe["updated_at"].dtype == "datetime64[ns, UTC]"
        assert steps_dataframe["started_at"].dtype == "datetime64[ns, UTC]"
        assert steps_dataframe["path_ids"].dtype == "object"
        assert isinstance(steps_dataframe["path_ids"].iloc[0], List)
        assert steps_dataframe["keywords"].dtype == "object"
        assert isinstance(steps_dataframe["keywords"].iloc[0], List)
        pd.testing.assert_frame_equal(
            steps_dataframe, expected_steps_dataframe, check_dtype=True
        )

    def test__convert_steps_to_dataframe_with_invalid_data_parameters__returns_only_step_data_without_measurement(
        self,
    ):
        """Test if the function returns a dataframe of steps with no measurement."""
        step_data = Step(
            name="step_name",
            step_id="5ffb2bf6771fa11e877838dd6",
            result_id="5ffb2bf6771fa11e877838dd8",
            data=StepData(
                text="data1",
                parameters=[Measurement(name="parameter_123", status="Passed")],
            ),
        )
        expected_column_order = [
            "name",
            "step_id",
            "result_id",
            "data.text",
        ]
        expected_steps_dataframe = self.__get_expected_steps_dataframe(
            [step_data], expected_column_order=expected_column_order
        )

        steps_dataframe = convert_steps_to_dataframe([step_data])

        assert not steps_dataframe.empty
        assert (
            steps_dataframe.columns.to_list()
            == expected_steps_dataframe.columns.to_list()
        )
        pd.testing.assert_frame_equal(
            steps_dataframe, expected_steps_dataframe, check_dtype=True
        )

    def test__convert_steps_to_dataframe_with_many_unset_measurement_fields__not_returns_unset_measurements_fields(
        self,
    ):
        step_data = Step(
            name="step_name",
            step_id="5ffb2bf6771fa11e877838dd6",
            result_id="5ffb2bf6771fa11e877838dd8",
            data=StepData(
                text="data1",
                parameters=[
                    Measurement(
                        name="parameter_11",
                        measurement="11.0",
                    ),
                    Measurement(
                        name="parameter_21",
                        measurement="11.3",
                    ),
                ],
            ),
        )
        expected_column_order = [
            "name",
            "step_id",
            "result_id",
            "data.text",
            "data.measurement.name",
            "data.measurement.measurement",
        ]
        expected_data_parameters = [
            [
                {
                    "data.measurement.name": "parameter_11",
                    "data.measurement.measurement": "11.0",
                },
                {
                    "data.measurement.name": "parameter_21",
                    "data.measurement.measurement": "11.3",
                },
            ]
        ]
        expected_steps_dataframe = self.__get_expected_steps_dataframe(
            [step_data],
            expected_column_order=expected_column_order,
            expected_data_parameters=expected_data_parameters,
        )

        steps_dataframe = convert_steps_to_dataframe([step_data])

        assert not steps_dataframe.empty
        assert (
            steps_dataframe.columns.to_list()
            == expected_steps_dataframe.columns.to_list()
        )
        pd.testing.assert_frame_equal(
            steps_dataframe, expected_steps_dataframe, check_dtype=True
        )

    def test__convert_steps_to_dataframe_with_none_callback__returns_step_with_all_data_parameters(
        self, mock_steps_data: List[Step]
    ):
        """Test normal case with valid step data."""
        expected_data_parameters = [
            [
                {
                    "data.parameters.name": "parameter_11",
                    "data.parameters.status": "Passed",
                    "data.parameters.measurement": "11.0",
                    "data.parameters.lowLimit": "6.0",
                    "data.parameters.highLimit": "21.0",
                    "data.parameters.units": "A",
                    "data.parameters.comparisonType": "GTLT",
                },
                {
                    "data.parameters.additionalProp": "myValue",
                },
            ],
            [
                {
                    "data.parameters.name": "parameter_21",
                    "data.parameters.status": "Passed",
                    "data.parameters.measurement": "11.0",
                    "data.parameters.lowLimit": "6.0",
                    "data.parameters.highLimit": "21.0",
                    "data.parameters.units": "A",
                    "data.parameters.comparisonType": "GTLT",
                    "data.parameters.additionalData": "additional_data_value",
                },
                {
                    "data.parameters.name": "parameter_22",
                    "data.parameters.status": "Passed",
                    "data.parameters.lowLimit": "7.0",
                    "data.parameters.highLimit": "22.0",
                    "data.parameters.units": "C",
                    "data.parameters.comparisonType": "GTLT",
                },
            ],
        ]
        expected_steps_dataframe = self.__get_expected_steps_dataframe(
            mock_steps_data,
            expected_data_parameters=expected_data_parameters,
            data_parameters_prefix="data.parameters",
        )

        steps_dataframe = convert_steps_to_dataframe(mock_steps_data, None)

        assert not steps_dataframe.empty
        assert (
            steps_dataframe.columns.to_list()
            == expected_steps_dataframe.columns.to_list()
        )

        assert steps_dataframe["updated_at"].dtype == "datetime64[ns, UTC]"
        assert steps_dataframe["started_at"].dtype == "datetime64[ns, UTC]"
        assert steps_dataframe["path_ids"].dtype == "object"
        assert isinstance(steps_dataframe["path_ids"].iloc[0], List)
        assert steps_dataframe["keywords"].dtype == "object"
        assert isinstance(steps_dataframe["keywords"].iloc[0], List)
        pd.testing.assert_frame_equal(
            steps_dataframe, expected_steps_dataframe, check_dtype=True
        )

    def __get_expected_results_dataframe(self, results: List[Result]):
        results_dict = []
        for result in results:
            status = {
                "status": (
                    result.status.status_type.value
                    if result.status and result.status.status_type != "CUSTOM"
                    else result.status.status_name if result.status else None
                )
            }
            status_type_summary = (
                {
                    f"status_type_summary.{key}": value
                    for key, value in result.status_type_summary.items()
                }
                if result.status_type_summary
                else {}
            )
            properties = (
                {f"properties.{key}": value for key, value in result.properties.items()}
                if result.properties
                else {}
            )
            results_dict.append(
                {
                    **{
                        "started_at": result.started_at,
                        "updated_at": result.updated_at,
                        "program_name": result.program_name,
                        "id": result.id,
                        "system_id": result.system_id,
                        "host_name": result.host_name,
                        "part_number": result.part_number,
                        "serial_number": result.serial_number,
                        "total_time_in_seconds": result.total_time_in_seconds,
                        "keywords": result.keywords,
                        "operator": result.operator,
                        "file_ids": result.file_ids,
                        "data_table_ids": result.data_table_ids,
                        "workspace": result.workspace,
                    },
                    **status,
                    **status_type_summary,
                    **properties,
                }
            )

        results_df = pd.DataFrame(results_dict)
        results_df = results_df[
            ["status"] + [col for col in results_df.columns if col != "status"]
        ]
        results_df.dropna(axis="columns", how="all", inplace=True)

        return results_df

    def __get_expected_steps_dataframe(
        self,
        mock_steps_data: List[Step],
        expected_data_parameters=None,
        expected_column_order=None,
        data_parameters_prefix="data.measurement",
    ) -> pd.DataFrame:
        steps_with_measurement_per_row = []
        index = 0
        for step in mock_steps_data:
            properties = (
                {f"properties.{key}": value for key, value in step.properties.items()}
                if step.properties
                else {}
            )
            inputs = (
                {f"inputs.{item.name}": item.value for item in step.inputs}
                if step.inputs
                else {}
            )
            outputs = (
                {f"outputs.{item.name}": item.value for item in step.outputs}
                if step.outputs
                else {}
            )
            for parameter in (
                expected_data_parameters[index]
                if (expected_data_parameters and expected_data_parameters[index])
                else [{}]
            ):
                steps_with_measurement_per_row.append(
                    {
                        "name": step.name,
                        "step_type": step.step_type,
                        "step_id": step.step_id,
                        "parent_id": step.parent_id,
                        "result_id": step.result_id,
                        "path": step.path,
                        "path_ids": step.path_ids,
                        "status": (
                            step.status.status_type.value
                            if step.status and step.status.status_type != "CUSTOM"
                            else step.status.status_name if step.status else None
                        ),
                        "total_time_in_seconds": step.total_time_in_seconds,
                        "started_at": step.started_at,
                        "updated_at": step.updated_at,
                        "data_model": step.data_model,
                        "has_children": step.has_children,
                        "workspace": step.workspace,
                        "keywords": step.keywords,
                        **inputs,
                        **outputs,
                        "data.text": step.data.text if step.data else None,
                        **{key: value for key, value in (parameter.items() or {})},
                        **properties,
                    }
                )
            index += 1

        steps_dataframe = pd.DataFrame(steps_with_measurement_per_row)

        dataframe_columns = [
            col
            for col in steps_dataframe.columns
            if col.startswith(data_parameters_prefix)
        ]
        default_column_order = [
            "name",
            "step_type",
            "step_id",
            "parent_id",
            "result_id",
            "path",
            "path_ids",
            "status",
            "total_time_in_seconds",
            "started_at",
            "updated_at",
            "data_model",
            "has_children",
            "workspace",
            "keywords",
            "inputs.Input00",
            "inputs.Input11",
            "inputs.Input12",
            "inputs.Input21",
            "inputs.Input22",
            "outputs.Output11",
            "outputs.Output12",
            "outputs.Output21",
            "outputs.Output22",
            "data.text",
            *dataframe_columns,
            "properties.property11",
            "properties.property12",
            "properties.property21",
            "properties.property22",
        ]
        return steps_dataframe.reindex(
            columns=expected_column_order or default_column_order, copy=False
        )
````
