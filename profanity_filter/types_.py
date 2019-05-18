from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Optional, Dict, Collection, Generator, Tuple, List, FrozenSet, Union

import spacy.language
from cached_property import cached_property
from hunspell_serializable import HunSpell
from pymorphy2 import MorphAnalyzer


class ProfanityFilterError(Exception):
    pass


@dataclass(frozen=True)
class Word:
    uncensored: str
    censored: str
    original_profane_word: Optional[str] = None

    def __str__(self):
        return self.censored

    @cached_property
    def is_profane(self) -> bool:
        return self.censored != self.uncensored


class AnalysisType(Enum):
    DEEP = 'deep'
    MORPHOLOGICAL = 'morphological'
    MULTILINGUAL = 'multilingual'


Words = Dict[str, Word]
AnalysesTypes = FrozenSet[AnalysisType]
Language = Optional[str]
ProfaneWordDictionary = 'OrderedSet[str]'
ProfaneWordDictionaryAcceptable = Collection[str]
ProfaneWordDictionaries = Dict[Language, ProfaneWordDictionary]
ProfaneWordDictionariesAcceptable = Optional[Dict[Language, ProfaneWordDictionaryAcceptable]]
Languages = 'OrderedSet[Language]'
LanguagesAcceptable = Collection[Language]
Nlps = Dict[Language, spacy.language.Language]
Morphs = Dict[Language, MorphAnalyzer]
Spells = Dict[Language, HunSpell]
Substrings = Generator[Tuple[str, int, int], Tuple[int, int], None]
TextSplittedByLanguage = List[Tuple[Language, str]]
PathOrStr = Union[Path, str]
