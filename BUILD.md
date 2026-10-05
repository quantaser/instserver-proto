# Building instserver-proto (.whl)

Pure Python package (compiled `_pb2.py` / `_pb2_grpc.py` stubs, no Cython, no platform
tag) — one wheel covers every Python/OS. Unlike `InstServer_grpc` / `InstServer_pyro4`
there is no Python-patch landmine here and no separate cp310/cp311 build.

## Build

```
python -m pip install build
python -m build
```

Output: `dist\instserver_proto-<ver>-py3-none-any.whl` (+ sdist `.tar.gz`).

## Regenerating the proto stubs (only when `protos/*.proto` changes)

```
python -m pip install grpcio-tools
python -m grpc_tools.protoc -I protos --python_out=instserver_proto --grpc_python_out=instserver_proto protos/instserver.proto
```
Commit the regenerated `instserver_pb2.py` / `instserver_pb2_grpc.py` — they ship as
plain source inside the wheel.

## Release: tag after bumping `pyproject.toml` version

Same manual-tag convention as `LabMaster3` (`LabMaster_<ver>`) and `InstServer_pyro4`
(`InstServer_<ver>`): every version bump in `pyproject.toml`'s `version = "..."` gets a
matching git tag once built:

```
git tag instserver-proto_<ver>
git push origin instserver-proto_<ver>
```

## Verify before shipping

Confirm the wheel has no platform tag and ships `.py` (not `.pyd`):
```
python -c "import zipfile;z=zipfile.ZipFile(r'dist\instserver_proto-<ver>-py3-none-any.whl');print('\n'.join(z.namelist()))"
```
Offline install check (no network):
```
pip install --no-index dist\instserver_proto-<ver>-py3-none-any.whl
```
