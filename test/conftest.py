import sys
import os
from pathlib import Path

sys.path.append(str(Path(os.path.dirname(__file__)).parent / "src"))
TESTS_DIR = Path(__file__).parent
