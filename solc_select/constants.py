import os
from pathlib import Path

# DIRs path
if "VIRTUAL_ENV" in os.environ:
    HOME_DIR = Path(os.environ["VIRTUAL_ENV"])
else:
    HOME_DIR = Path.home()
SOLC_SELECT_DIR = HOME_DIR.joinpath(".solc-select")
ARTIFACTS_DIR = SOLC_SELECT_DIR.joinpath("artifacts")

# CLI Flags
INSTALL_VERSIONS = "INSTALL_VERSIONS"
USE_VERSION = "USE_VERSION"
SHOW_VERSIONS = "SHOW_VERSIONS"
UPGRADE = "UPGRADE"

LINUX_AMD64 = "linux-amd64"
MACOSX_AMD64 = "macosx-amd64"
WINDOWS_AMD64 = "windows-amd64"
LINUX_AMD64 = "linux-amd64"
LINUX_AARCH64 = "linux-aarch64"

EARLIEST_RELEASE = {
        "macosx-amd64": "0.3.6",
        "linux-amd64": "0.4.0",
        "windows-amd64": "0.4.5",
        "linux-aarch64": "0.5.0"
}

# URL
CRYTIC_SOLC_ARTIFACTS = "https://raw.githubusercontent.com/crytic/solc/master/linux/amd64/"
CRYTIC_SOLC_JSON = (
    "https://raw.githubusercontent.com/crytic/solc/new-list-json/linux/amd64/list.json"
)
# copied from svm-rs:
# https://github.com/alloy-rs/svm-rs/blob/08664e0653d6ecd887b62f6d5a31c358722718f0/crates/svm-rs/src/releases.rs#L34-L38
LINUX_AARCH64_SOLC_ARTIFACTS =
    "https://github.com/nikitastupin/solc/raw/fd781c58fe3abb978749bb3184405d1fe7c4cd26/linux/aarch64"
LINUX_AARCH64_SOLC_JSON =
    "https://github.com/nikitastupin/solc/raw/fd781c58fe3abb978749bb3184405d1fe7c4cd26/linux/aarch64/list.json"
