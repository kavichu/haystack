import pytest

from haystack.dataclasses import StreamingChunk


def test_create_chunk_with_content_and_metadata():
    chunk = StreamingChunk(content="Test content", metadata={"key": "value"})

    assert chunk.content == "Test content"
    assert chunk.metadata == {"key": "value"}


def test_create_chunk_with_only_content():
    chunk = StreamingChunk(content="Test content")

    assert chunk.content == "Test content"
    assert chunk.metadata == {}


def test_access_content():
    chunk = StreamingChunk(content="Test content", metadata={"key": "value"})
    assert chunk.content == "Test content"


def test_create_chunk_with_empty_content():
    chunk = StreamingChunk(content="")
    assert chunk.content == ""
    assert chunk.metadata == {}
