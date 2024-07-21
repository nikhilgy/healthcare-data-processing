{{ config(materialized='table') }}

select 
    CAST(start as date) as onset_date,
    CAST(stop as date) as resolved_date,
    CAST(patient as uuid) as patient_id,
    CAST(encounter as uuid) as encounter_id,
    CAST(code as bigint) as source_code,
    description as source_description
from {{ source('lupus_staging_raw', 'conditions') }}

