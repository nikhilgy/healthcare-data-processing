{{ config(materialized='table') }}

select 
    CAST(start as date) as prescribing_date,
    CAST(patient as uuid) as patient_id,
    CAST(encounter as uuid) as encounter_id,
    CAST(code as varchar) as ndc_code,
    description as ndc_description,
    CAST(reasoncode as varchar) as source_code,
    reasondescription as source_description
from {{ source('lupus_staging_raw', 'medications') }}

