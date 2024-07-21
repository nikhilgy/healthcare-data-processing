{{ config(materialized='table') }}

select 
    CAST(id as uuid) as encounter_id,
    CAST(start as date) as encounter_start_date,
    CAST(stop as date) as encounter_stop_date,
    CAST(patient as uuid) as patient_id,
    CAST(organization as uuid) as facility_id,
    CAST(provider as uuid) as attending_provider_id,
    CAST(encounterclass as varchar) as encounter_type,
    CAST(code as varchar) as admit_type_code,
    CAST(description as varchar) as admit_type_description,
    CAST(base_encounter_cost as numeric) as allowed_amount,
    CAST(total_claim_cost as numeric) as charge_amount,
    CAST(payer_coverage as numeric) as paid_amount,
    CAST(reasoncode as varchar) as admit_source_code,
    CAST(reasondescription as varchar) as admit_source_description
from {{ source('lupus_staging_raw', 'encounters') }}

