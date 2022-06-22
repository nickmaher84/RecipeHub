SELECT
    raw.spider,
    raw.url,
    raw.language,
    raw.checksum,
    raw.timestamp,
    row.key,
    row.value
FROM
    {{ source('raw', 'recipe') }} AS raw,
    json_each(raw.json) row(key, value)