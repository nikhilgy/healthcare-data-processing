{{ config(materialized='table') }}

select 
    CAST(patient_id as uuid) as patient_id,
    CAST(first_name as varchar) as first_name,
    CAST(last_name as varchar) as last_name,
    CAST(gender as varchar) as sex,
    CAST(race as varchar) as race,
    CAST(birthdate as date) as birth_date,
    CAST(deathdate as date) as death_date,
    CAST(ssn as varchar) as social_security_number,
    CAST(address as varchar) as address,
    CAST(city as varchar) as city,
    CAST(state as varchar) as state,
    CAST(zip as varchar) as zip_code,
    CAST(county as varchar) as county,
    CAST(lat as numeric) as latitude,
    CAST(lon as numeric) as longitude
from {{ source('lupus_staging_raw', 'patients') }}

