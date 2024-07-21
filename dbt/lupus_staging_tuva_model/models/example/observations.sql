{{ config(materialized='table') }}

select 
    CAST(patient as uuid) as patient_id,
    CAST(COALESCE(NULLIF(split_part(split_part(symptoms, 'Rash:', 2), ';', 1), ''), '0') as INTEGER) AS Rash,
    CAST(COALESCE(NULLIF(split_part(split_part(symptoms, 'Joint Pain:', 2), ';', 1), ''), '0') as INTEGER) AS Joint_Pain,
    CAST(COALESCE(NULLIF(split_part(split_part(symptoms, 'Fatigue:', 2), ';', 1), ''), '0') as INTEGER) AS Fatigue,
    CAST(COALESCE(NULLIF(split_part(split_part(symptoms, 'Fever:', 2), ';', 1), ''), '0') as INTEGER) AS Fever
from {{ source('lupus_staging_raw', 'symptoms') }}

