"""
The default attribute of module :
    "name"   :"default",            # Module 이름
    "author" :"carpe",              # Module 제작자
    "ver"    :"0.0",                # Module 버젼
    "param"  :None,                 # Module 파라미터
    "encode" :"utf-8",              # Module 인코딩
    "base"   :0                     # File image base to carve

"""
import os

# 정적 설정
# 동적인 설정은 ModuleConfiguration을 이용하여 config.txt에 기록!
# --> module_config.py

class ModuleConstant(object):
    # System Environment
    LIB_DEFAULT_PATH = "/usr/local/lib/"
    DEFINE_PATH      = os.path.abspath(os.path.dirname(__file__))+os.sep

    # Module Attribute
    NAME             = "name"
    AUTHOR           = "author"
    VERSION          = "ver"
    ID               = "id"
    PARAMETER        = "param"
    ENCODE           = "encode"
    FILE_ATTRIBUTE   = "file"
    IMAGE_BASE       = "base"
    IMAGE_LAST       = "last"
    EXCLUSIVE        = "excl"
    CLUSTER_SIZE     = "cluster"

    # Confiugration Operations
    COLLABORATE      = 6
    CONFIG_FILE      = "config.txt"
    INIT             = 0b00000000
    READ             = 0b00000001
    WRITE            = 0b00000010
    CREATE           = 0b00000100
    DELETE           = 0b00001000
    SAVE             = 0b00010000

    # Page Type
    FILE_HEADER      = 0b00000001
    FILE_RECORD      = 0b00000010
    FILE_ONESHOT     = 0b00000100
    INVALID          = 0b10000000

    # Error
    class Return(object):
        SUCCESS          = 0    # 성공
        EINVAL_ATTRIBUTE = -1   # Invalid attribute
        EINVAL_FILE      = -2   # Invalid file input
        EINVAL_TYPE      = -3   # Invalid data type
        EINVAL_NONE      = -4   # Nothing to getw

    # Dependency List (Static)
    class Dependency(object):
        pecarve          = "pecarve"