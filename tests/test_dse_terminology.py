"""Public architectural wording checks for manager-approved DEC-GRD-021."""
from __future__ import annotations

from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
CANONICAL = [
    ROOT / "README.md",
    ROOT / "docs/architecture.md",
    ROOT / "docs/principles.md",
    ROOT / "docs/governance.md",
]
RELATED_WORK = ROOT / "references/related-work.md"
MAPPING = ROOT / "docs/terminology-migration-2026-10-27.md"


class DSECanonicalTermTests(unittest.TestCase):
    def test_reference_documents_use_canonical_term(self):
        for p in CANONICAL:
            with self.subTest(path=str(p.relative_to(ROOT))):
                content = p.read_text(encoding="utf-8")
                self.assertIn("Digital Sovereign Entity", content)
                if p.name != "architecture.md":
                    self.assertNotIn("Sovereign Digital Entity", content)

    def test_architecture_defines_exact_historical_alias(self):
        arch = (ROOT / "docs/architecture.md").read_text(encoding="utf-8")
        self.assertIn("Digital Sovereign Entity (DSE)", arch)
        self.assertIn("Sovereign Digital Entity", arch)
        self.assertIn("same conceptual entity", arch)
        self.assertIn("Entidade Digital Soberana (EDS)", arch)

    def test_explicit_mapping_preserves_ontology(self):
        mapping = MAPPING.read_text(encoding="utf-8")
        for required in [
            "Digital Sovereign Entity (DSE)",
            "Sovereign Digital Entity",
            "the same concept",
            "not a new protocol identifier",
            "Authority does not equal",
            "does not rename any API field",
        ]:
            with self.subTest(required=required):
                self.assertIn(required, mapping)

    def test_related_work_descriptive_usage_aligned(self):
        content = RELATED_WORK.read_text(encoding="utf-8")
        self.assertIn("digital sovereign entity", content)
        self.assertNotIn("sovereign digital entity", content)


if __name__ == "__main__":
    unittest.main()
