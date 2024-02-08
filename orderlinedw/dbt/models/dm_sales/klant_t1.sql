{{ config(materialized='table') }}

SELECT
    *
FROM {{ ref('orderline_staging', 'klant') }}

