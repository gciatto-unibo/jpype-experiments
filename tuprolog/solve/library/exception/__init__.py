from tuprolog import logger

# noinspection PyUnresolvedReferences
import jpype
# noinspection PyUnresolvedReferences
import jpype.imports

# noinspection PyUnresolvedReferences
from it.unibo.tuprolog.solve.library.exception import AlreadyLoadedLibraryException
# noinspection PyUnresolvedReferences
from it.unibo.tuprolog.solve.library.exception import LibraryException
# noinspection PyUnresolvedReferences
from it.unibo.tuprolog.solve.library.exception import NoSuchALibraryException


logger.debug("Loaded JVM classes from it.unibo.tuprolog.solve.library.exception.*")
