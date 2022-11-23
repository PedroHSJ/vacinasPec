def selectVacina(codibge):
    return f'''
Select Distinct
-- Cast(Date_Part('year', Age(tb_fat_vacinacao.dt_nascimento)) As Int) As idade,
    tb_fat_cidadao_pec.co_cidadao,
    case when tb_fat_cidadao_pec.co_dim_sexo = 1 then 'Masculino'
    when tb_fat_cidadao_pec.co_dim_sexo = 2 then 'Feminino' end as sexo,
   tb_fat_cidadao_pec.nu_cpf_cidadao as cpf_cidadao,
    tb_fat_cidadao_pec.nu_cns,
    tb_fat_cidadao_pec.no_cidadao,
 
    Case
        When tb_dim_imunobiologico.no_imunobiologico = 'Covid-19 - BNT162b2 - BioNTech/Fosun Pharma/Pfizer' And
            tb_dim_dose_imunobiologico.sg_dose_imunobiologico = 'D1'
        Then tb_dim_tempo.dt_registro
    End As covid_pfizer_primeira_dose,
    Case
        When tb_dim_imunobiologico.no_imunobiologico = 'Covid-19 - BNT162b2 - BioNTech/Fosun Pharma/Pfizer' And
            tb_dim_dose_imunobiologico.sg_dose_imunobiologico = 'D2'
        Then tb_dim_tempo.dt_registro
    End As covid_pfizer_segunda_dose,
    Case
        When tb_dim_imunobiologico.no_imunobiologico = 'Covid-19 - BNT162b2 - BioNTech/Fosun Pharma/Pfizer' And
            tb_dim_dose_imunobiologico.sg_dose_imunobiologico = 'REF'
        Then tb_dim_tempo.dt_registro
    End As covid_pfizer_dose_reforco,
     Case
        When tb_dim_imunobiologico.no_imunobiologico = 'Covid-19 - BNT162b2 - BioNTech/Fosun Pharma/Pfizer' And
            tb_dim_dose_imunobiologico.sg_dose_imunobiologico = 'R2'
        Then tb_dim_tempo.dt_registro
    End As covid_pfizer_segunda_dose_reforco,
     Case
        When tb_dim_imunobiologico.no_imunobiologico = 'Covid-19 - BNT162b2 - BioNTech/Fosun Pharma/Pfizer' And
            tb_dim_dose_imunobiologico.sg_dose_imunobiologico = 'R3'
        Then tb_dim_tempo.dt_registro
    End As covid_pfizer_terceira_dose_reforco,
    Case
        When tb_dim_imunobiologico.no_imunobiologico = 'Covid-19 - BNT162b2 - BioNTech/Fosun Pharma/Pfizer' And
            tb_dim_dose_imunobiologico.sg_dose_imunobiologico = 'DA'
        Then tb_dim_tempo.dt_registro
    End As covid_pfizer_dose_adicional,
  
    Case
        When tb_dim_imunobiologico.no_imunobiologico = 'BCG'
        Then tb_dim_tempo.dt_registro
    End As BCG,
    Case
        When tb_dim_imunobiologico.no_imunobiologico = 'Hepatite B' And
            tb_dim_dose_imunobiologico.sg_dose_imunobiologico = 'D'
        Then tb_dim_tempo.dt_registro
    End As Hepatite_Dose,
    Case
        When tb_dim_imunobiologico.no_imunobiologico = 'Hepatite B' And
            tb_dim_dose_imunobiologico.sg_dose_imunobiologico = 'D1'
        Then tb_dim_tempo.dt_registro
    End As Hepatite_primeira_Dose,
    Case
        When tb_dim_imunobiologico.no_imunobiologico = 'Hepatite B' And
            tb_dim_dose_imunobiologico.sg_dose_imunobiologico = 'D2'
        Then tb_dim_tempo.dt_registro
    End As Hepatite_segunda_Dose,
    Case
        When tb_dim_imunobiologico.no_imunobiologico = 'Hepatite B' And
            tb_dim_dose_imunobiologico.sg_dose_imunobiologico = 'D3'
        Then tb_dim_tempo.dt_registro
    End As Hepatite_terceira_Dose,
    Case
        When tb_dim_imunobiologico.no_imunobiologico = 'Hepatite B' And
            tb_dim_dose_imunobiologico.sg_dose_imunobiologico = 'REV'
        Then tb_dim_tempo.dt_registro
    End As Hepatite_revacinacao,
    Case
        When tb_dim_imunobiologico.no_imunobiologico = 'DTP / HB / Hib' And
            tb_dim_dose_imunobiologico.sg_dose_imunobiologico = 'D1'
        Then tb_dim_tempo.dt_registro
    End As Pentavalente_primeira_dose,
    Case
        When tb_dim_imunobiologico.no_imunobiologico = 'DTP / HB / Hib' And
            tb_dim_dose_imunobiologico.sg_dose_imunobiologico = 'D2'
        Then tb_dim_tempo.dt_registro
    End As Pentavalente_segunda_dose,
    Case
        When tb_dim_imunobiologico.no_imunobiologico = 'DTP / HB / Hib' And
            tb_dim_dose_imunobiologico.sg_dose_imunobiologico = 'D3'
        Then tb_dim_tempo.dt_registro
    End As Pentavalente_terceira_dose,
    Case
        When tb_dim_imunobiologico.no_imunobiologico = 'Tríplice bacteriana' And
            tb_dim_dose_imunobiologico.sg_dose_imunobiologico = 'R1'
        Then tb_dim_tempo.dt_registro
    End As dtp_primeira_reforco,
    Case
        When tb_dim_imunobiologico.no_imunobiologico = 'Tríplice bacteriana' And
            tb_dim_dose_imunobiologico.sg_dose_imunobiologico = 'R2'
        Then tb_dim_tempo.dt_registro
    End As dtp_segunda_reforco,
    Case
        When tb_dim_imunobiologico.no_imunobiologico = 'Poliomielite inativada' And
            tb_dim_dose_imunobiologico.sg_dose_imunobiologico = 'D1'
        Then tb_dim_tempo.dt_registro
    End As Poliomielite_primeira_dose,
    Case
        When tb_dim_imunobiologico.no_imunobiologico = 'Poliomielite inativada' And
            tb_dim_dose_imunobiologico.sg_dose_imunobiologico = 'D2'
        Then tb_dim_tempo.dt_registro
    End As Poliomielite_segunda_dose,
    Case
        When tb_dim_imunobiologico.no_imunobiologico = 'Poliomielite inativada' And
            tb_dim_dose_imunobiologico.sg_dose_imunobiologico = 'D3'
        Then tb_dim_tempo.dt_registro
    End As Poliomielite_terceira_dose,
    Case
        When tb_dim_imunobiologico.no_imunobiologico = 'Poliomielite oral (Bivalente)' And
            tb_dim_dose_imunobiologico.sg_dose_imunobiologico = 'R1'
        Then tb_dim_tempo.dt_registro
    End As Poliomielite_primeira_reforco,
    Case
        When tb_dim_imunobiologico.no_imunobiologico = 'Poliomielite oral (Bivalente)' And
            tb_dim_dose_imunobiologico.sg_dose_imunobiologico = 'R2'
        Then tb_dim_tempo.dt_registro
    End As Poliomielite_segunda_reforco,
    Case
        When tb_dim_imunobiologico.no_imunobiologico = 'Pneumocócica 10V' And
            tb_dim_dose_imunobiologico.sg_dose_imunobiologico = 'D1'
        Then tb_dim_tempo.dt_registro
    End As Pneumococica_primeira_dose,
    Case
        When tb_dim_imunobiologico.no_imunobiologico = 'Pneumocócica 10V' And
            tb_dim_dose_imunobiologico.sg_dose_imunobiologico = 'D2'
        Then tb_dim_tempo.dt_registro
    End As Pneumococica_segunda_dose,
    Case
        When tb_dim_imunobiologico.no_imunobiologico = 'Pneumocócica 10V' And
            tb_dim_dose_imunobiologico.sg_dose_imunobiologico = 'REF'
        Then tb_dim_tempo.dt_registro
    End As Pneumococica_reforco,
    Case
        When tb_dim_imunobiologico.no_imunobiologico = 'Vacina rotavírus humano' And
            tb_dim_dose_imunobiologico.sg_dose_imunobiologico = 'D1'
        Then tb_dim_tempo.dt_registro
    End As rotavirus_humano_primeira_dose,
    Case
        When tb_dim_imunobiologico.no_imunobiologico = 'Vacina rotavírus humano' And
            tb_dim_dose_imunobiologico.sg_dose_imunobiologico = 'D2'
        Then tb_dim_tempo.dt_registro
    End As rotavirus_humano_segunda_dose,
    Case
        When tb_dim_imunobiologico.no_imunobiologico = 'Meningocócica conjugada C' And
            tb_dim_dose_imunobiologico.sg_dose_imunobiologico = 'D1'
        Then tb_dim_tempo.dt_registro
    End As meningococica_primeira_dose,
    Case
        When tb_dim_imunobiologico.no_imunobiologico = 'Meningocócica conjugada C' And
            tb_dim_dose_imunobiologico.sg_dose_imunobiologico = 'D2'
        Then tb_dim_tempo.dt_registro
    End As meningococica_segunda_dose,
    Case
        When tb_dim_imunobiologico.no_imunobiologico = 'Meningocócica conjugada C' And
            tb_dim_dose_imunobiologico.sg_dose_imunobiologico = 'R1'
        Then tb_dim_tempo.dt_registro
    End As meningococica_primeira_dose_reforco,
    Case
        When tb_dim_imunobiologico.no_imunobiologico = 'Meningocócica conjugada C' And
            tb_dim_dose_imunobiologico.sg_dose_imunobiologico = 'R2'
        Then tb_dim_tempo.dt_registro
    End As meningococica_segunda_dose_reforco,
    Case
        When tb_dim_imunobiologico.no_imunobiologico = 'Meningocócica conjugada C' And
            tb_dim_dose_imunobiologico.sg_dose_imunobiologico = 'DU'
        Then tb_dim_tempo.dt_registro
    End As meningococica_dose_unica,
    Case
        When tb_dim_imunobiologico.no_imunobiologico = 'Febre amarela' And
            tb_dim_dose_imunobiologico.sg_dose_imunobiologico = 'D1'
        Then tb_dim_tempo.dt_registro
    End As febre_amarela_primeira_dose,
    Case
        When tb_dim_imunobiologico.no_imunobiologico = 'Febre amarela' And
            tb_dim_dose_imunobiologico.sg_dose_imunobiologico = 'REF'
        Then tb_dim_tempo.dt_registro
    End As febre_amarela_dose_reforco,
    Case
        When (tb_dim_imunobiologico.no_imunobiologico = 'Hepatite A (CRIE)' 
        or tb_dim_imunobiologico.no_imunobiologico = 'Hepatite A Pediátrica')
        And
            tb_dim_dose_imunobiologico.sg_dose_imunobiologico = 'D1'
        Then tb_dim_tempo.dt_registro
    End As hepatite_a_primeira_dose,
    Case
        When tb_dim_imunobiologico.no_imunobiologico = 'Tríplice viral' And
            tb_dim_dose_imunobiologico.sg_dose_imunobiologico = 'D1'
        Then tb_dim_tempo.dt_registro
    End As triciple_viral_primeira_dose,
    Case
        When tb_dim_imunobiologico.no_imunobiologico = 'Tríplice viral' And
            tb_dim_dose_imunobiologico.sg_dose_imunobiologico = 'D2'
        Then tb_dim_tempo.dt_registro
    End As triciple_viral_segunda_dose,
    Case
        When tb_dim_imunobiologico.no_imunobiologico = 'Tetra Viral' And
            tb_dim_dose_imunobiologico.sg_dose_imunobiologico = 'DU'
        Then tb_dim_tempo.dt_registro
    End As Tetra_viral_dose_unica, 
    Case
        When tb_dim_imunobiologico.no_imunobiologico = 'Varicela (atenuada)' And
            tb_dim_dose_imunobiologico.sg_dose_imunobiologico = 'D1'
        Then tb_dim_tempo.dt_registro
    End As varicela_primeira_dose,
    Case
        When tb_dim_imunobiologico.no_imunobiologico = 'Varicela (atenuada)' And
            tb_dim_dose_imunobiologico.sg_dose_imunobiologico = 'D2'
        Then tb_dim_tempo.dt_registro
    End As varicela_segunda_dose,
     case When (tb_dim_imunobiologico.no_imunobiologico = 'HPV Bivalente' or
      tb_dim_imunobiologico.no_imunobiologico = 'HPV Quadrivalente')
      And
            tb_dim_dose_imunobiologico.sg_dose_imunobiologico = 'D1'
        Then tb_dim_tempo.dt_registro
    End As hpv_primeira_dose,
     case When (tb_dim_imunobiologico.no_imunobiologico = 'HPV Bivalente' or
      tb_dim_imunobiologico.no_imunobiologico = 'HPV Quadrivalente')
      And
            tb_dim_dose_imunobiologico.sg_dose_imunobiologico = 'D2'
        Then tb_dim_tempo.dt_registro
    End As hpv_segunda_dose,
     
    Case
        When tb_dim_imunobiologico.no_imunobiologico = 'Meningocócica ACWY' And
            tb_dim_dose_imunobiologico.sg_dose_imunobiologico = 'D'
        Then tb_dim_tempo.dt_registro
    End As meningococia_dose,
    Case
        When tb_dim_imunobiologico.no_imunobiologico = 'Meningocócica ACWY' And
            tb_dim_dose_imunobiologico.sg_dose_imunobiologico = 'REF'
        Then tb_dim_tempo.dt_registro
    End As meningococia_dose_reforco, 
       tb_fat_vacinacao.dt_nascimento,
    tb_dim_unidade_saude.nu_cnes,
    tb_dim_unidade_saude.no_unidade_saude,
    tb_dim_equipe.nu_ine,
    tb_dim_equipe.no_equipe,
    tb_dim_profissional.no_profissional,
    tb_dim_municipio.no_municipio,
    tb_dim_municipio.co_ibge,
    tb_dim_uf.sg_uf,
    tb_dim_tempo.dt_registro
    -- tb_fat_cidadao_pec.nu_telefone_celular
    
From
    tb_fat_vacinacao Left Join
    tb_fat_cidadao_pec On tb_fat_vacinacao.co_fat_cidadao_pec = tb_fat_cidadao_pec.co_seq_fat_cidadao_pec Left Join
    tb_dim_faixa_etaria On tb_fat_vacinacao.co_dim_faixa_etaria = tb_dim_faixa_etaria.co_seq_dim_faixa_etaria Left Join
    tb_fat_vacinacao_vacina On tb_fat_vacinacao_vacina.co_fat_vacinacao = tb_fat_vacinacao.co_seq_fat_vacinacao
    Left Join
    tb_dim_dose_imunobiologico On tb_fat_vacinacao_vacina.co_dim_dose_imunobiologico =
            tb_dim_dose_imunobiologico.co_seq_dim_dose_imunobiologico Left Join
    tb_dim_imunobiologico On tb_fat_vacinacao_vacina.co_dim_imunobiologico =
            tb_dim_imunobiologico.co_seq_dim_imunobiologico Left Join
    tb_dim_unidade_saude On tb_fat_vacinacao_vacina.co_dim_unidade_saude = tb_dim_unidade_saude.co_seq_dim_unidade_saude
    Left Join
    tb_dim_equipe On tb_fat_vacinacao_vacina.co_dim_equipe = tb_dim_equipe.co_seq_dim_equipe Left Join
    tb_dim_profissional On tb_fat_vacinacao_vacina.co_dim_profissional = tb_dim_profissional.co_seq_dim_profissional
    Left Join
    tb_dim_municipio On tb_fat_vacinacao_vacina.co_dim_municipio = tb_dim_municipio.co_seq_dim_municipio Left Join
    tb_dim_uf On tb_dim_municipio.co_dim_uf = tb_dim_uf.co_seq_dim_uf Left Join
    tb_fat_atendimento_individual On tb_fat_atendimento_individual.co_fat_cidadao_pec =
            tb_fat_cidadao_pec.co_seq_fat_cidadao_pec Left Join
    tb_dim_tempo On tb_fat_vacinacao_vacina.co_dim_tempo = tb_dim_tempo.co_seq_dim_tempo
 Where 
     tb_dim_municipio.co_ibge = '{codibge}'    and
    tb_fat_vacinacao.dt_nascimento >= current_date - interval '15' year
    order by tb_dim_tempo.dt_registro desc
    '''