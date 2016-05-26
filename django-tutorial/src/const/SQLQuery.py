#  Query data for prediction by condition "Candidate_email" and "Employer_name":
# + candidate_name,
# + candidate_emloyment_job_start
# + candidate_employment_job_end
# + candidate_degree
# + candidate_gender

candidate_data_by_email_employer = "SELECT" \
                                    "can.candidate_id," \
                                    "can.candidate_email,"\
                                    "em.c_employment_employer_name,"\
                                    "em.c_employment_job_start,"\
                                    "em.c_employment_job_end,"\
                                    "eth.name "\
                                    "FROM candidates can "\
                                    "LEFT JOIN c_employment em ON em.c_employment_candidate_id=can.candidate_id "\
                                    "INNER JOIN c_details de ON de.c_details_candidate_id = can.candidate_id "\
                                    "LEFT JOIN ethnicity eth ON eth.id = can.candidate_ethnicity_id "\
                                    "WHERE can.candidate_email = '%s' "\
                                    "AND upper(em.c_employment_employer_name) = upper('%s')"


# Query candidate data by email
candidate_data_by_email = "SELECT"\
                            "can.candidate_id,"\
                            "can.candidate_email,"\
                            "em.c_employment_employer_name,"\
                            "em.c_employment_job_start,"\
                            "em.c_employment_job_end,"\
                            "eth.name "\
                            "FROM candidates can "\
                            "LEFT JOIN c_employment em ON em.c_employment_candidate_id=can.candidate_id "\
                            "INNER JOIN c_details de ON de.c_details_candidate_id = can.candidate_id "\
                            "LEFT JOIN ethnicity eth ON eth.id = can.candidate_ethnicity_id "\
                            "WHERE can.candidate_email = '%s'"

# Query fortune Company by Employer's name

fortune_company = "SELECT fortune_company_name "\
                    "FROM fortune_company "\
                    "WHERE upper(fortune_company_name) = upper('%s')"