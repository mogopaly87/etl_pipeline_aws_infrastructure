import configparser


# CONFIG
config = configparser.ConfigParser()
config.read("dwh.cfg")

ARN = config.get("IAM_ROLE", "ARN")
LOG_DATA = config.get("S3", "LOG_DATA")
LOG_JSONPATH = config.get("S3", "LOG_JSONPATH")
SONGS_DATA = config.get("S3", "SONGS_DATA")
# SONGS_JSONPATH = config.get("S3", "SONGS_JSONPATH")

# DROP TABLES

staging_events_table_drop = "DROP TABLE IF EXISTS staging_events"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_songs"
songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

staging_events_table_create = """
    CREATE TABLE "staging_events"(
        event_id BIGINT IDENTITY(0, 1) NOT NULL,
        artist VARCHAR NULL,
        auth VARCHAR NULL,
        firstName VARCHAR NULL,
        gender VARCHAR NULL,
        itemInSession VARCHAR NULL,
        lastName VARCHAR NULL,
        length VARCHAR NULL,
        level VARCHAR NULL,
        location VARCHAR NULL,
        method VARCHAR NULL,
        page VARCHAR NULL,
        registration VARCHAR NULL,
        sessionId INTEGER NOT NULL SORTKEY DISTKEY,
        song VARCHAR NULL,
        status VARCHAR NULL,
        ts BIGINT NOT NULL,
        userAgent VARCHAR NULL,
        userId INTEGER NULL
        );
"""

staging_songs_table_create = """
    CREATE TABLE IF NOT EXISTS staging_songs(
        song_id     VARCHAR      NOT NULL,
        num_songs   INTEGER         NULL,
        title       VARCHAR(500)   NULL,
        artist_name VARCHAR(500)   NULL,
        artist_latitude  VARCHAR    NULL,
        year        INTEGER         NULL,
        duration    DECIMAL(9)      NULL,
        artist_id   VARCHAR         NOT NULL SORTKEY DISTKEY,
        artist_longitude VARCHAR    NULL,
        artist_location  VARCHAR(500)  NULL
        );
"""

songplay_table_create = """
    CREATE TABLE IF NOT EXISTS songplays(
        songplay_id BIGINT IDENTITY(0,1) NOT NULL,
        start_time TIMESTAMP NOT NULL,
        user_id INTEGER NOT NULL,
        level VARCHAR NOT NULL,
        song_id VARCHAR NOT NULL,
        artist_id VARCHAR NOT NULL,
        session_id INTEGER NOT NULL,
        location VARCHAR,
        user_agent VARCHAR(255)
    );
"""

user_table_create = """
    CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER NOT NULL SORTKEY,
        first_name VARCHAR(100) NULL,
        last_name VARCHAR(100) NULL,
        gender VARCHAR(10) NULL,
        level VARCHAR(10) NULL
    );
"""

song_table_create = """
    CREATE TABLE IF NOT EXISTS songs (
        song_id VARCHAR(50) NOT NULL SORTKEY,
        title VARCHAR(400) NOT NULL,
        artist_id VARCHAR(50) NOT NULL,
        year INTEGER NOT NULL,
        duration NUMERIC NOT NULL
    );
"""

artist_table_create = """
    CREATE TABLE IF NOT EXISTS artists (
        artist_id VARCHAR(50) NOT NULL SORTKEY,
        name VARCHAR(500) NULL,
        location VARCHAR(400) NULL,
        latitude NUMERIC NULL,
        longitude NUMERIC NULL
    ) diststyle ALL;
"""

time_table_create = """
    CREATE TABLE IF NOT EXISTS time(
        start_time TIMESTAMP NOT NULL SORTKEY,
        hour SMALLINT NULL,
        day SMALLINT NULL,
        week SMALLINT NULL, 
        month SMALLINT NULL,
        year SMALLINT NULL,
        weekday SMALLINT NULL
    );
"""

# STAGING TABLES

staging_events_copy = (
    """
    COPY staging_events FROM {}
    iam_role '{}'
    format as json {}
    STATUPDATE ON
    region 'us-west-2';
"""
).format(LOG_DATA, ARN, LOG_JSONPATH)

staging_songs_copy = (
    """
    COPY staging_songs FROM {}
    iam_role '{}'
    FORMAT AS JSON 'auto'
    STATUPDATE ON
    ACCEPTINVCHARS AS '^'
    region 'us-west-2';
"""
).format(SONGS_DATA, ARN)

# FINAL TABLES

songplay_table_insert = """
"""

user_table_insert = """
"""

song_table_insert = """
"""

artist_table_insert = """
"""

time_table_insert = """
"""

# QUERY LISTS

create_table_queries = [
    staging_events_table_create,
    staging_songs_table_create,
    songplay_table_create,
    user_table_create,
    song_table_create,
    artist_table_create,
    time_table_create,
]
drop_table_queries = [
    staging_events_table_drop,
    staging_songs_table_drop,
    songplay_table_drop,
    user_table_drop,
    song_table_drop,
    artist_table_drop,
    time_table_drop,
]
copy_table_queries = [staging_events_copy, staging_songs_copy]  # , staging_songs_copy
insert_table_queries = [
    songplay_table_insert,
    user_table_insert,
    song_table_insert,
    artist_table_insert,
    time_table_insert,
]
