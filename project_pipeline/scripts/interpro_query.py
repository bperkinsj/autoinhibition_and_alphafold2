'''
For drafts of interpro queries.
'''
uniprot = df.loc[i, 'uniprot']

url = f'https://www.ebi.ac.uk/interpro/api/entry/protein/uniprot/{uniprot}/'
# This returns something that looks like the json entry at the bottom.
# Our challenge will be to select which type we want. I am leaning toward family, which may be sufficiently exact and broad.
# Our data structure would look like:
'''
interpro    type    name
IPR002117   family  p53 tumor suppressor family
'''
# That way we can cluster by interpro accession but still have human-readable labels. 
'''
{
    "count": 8,
    "next": null,
    "previous": null,
    "results": [
        {
            "metadata": {
                "accession": "IPR002117",
                "name": "p53 tumour suppressor family",
                "source_database": "interpro",
                "type": "family",
                "integrated": null,
                "member_databases": {
                    "prosite": {
                        "PS00348": "p53 family signature"
                    },
                    "panther": {
                        "PTHR11447": "CELLULAR TUMOR ANTIGEN P53"
                    },
                    "prints": {
                        "PR00386": "P53SUPPRESSR"
                    }
                },
                "go_terms": [
                    {
                        "identifier": "GO:0003677",
                        "name": "DNA binding",
                        "category": {
                            "code": "F",
                            "name": "molecular_function"
                        }
                    },
                    {
                        "identifier": "GO:0003700",
                        "name": "DNA-binding transcription factor activity",
                        "category": {
                            "code": "F",
                            "name": "molecular_function"
                        }
                    },
                    {
                        "identifier": "GO:0006355",
                        "name": "regulation of DNA-templated transcription",
                        "category": {
                            "code": "P",
                            "name": "biological_process"
                        }
                    },
                    {
                        "identifier": "GO:0006915",
                        "name": "apoptotic process",
                        "category": {
                            "code": "P",
                            "name": "biological_process"
                        }
                    },
                    {
                        "identifier": "GO:0005634",
                        "name": "nucleus",
                        "category": {
                            "code": "C",
                            "name": "cellular_component"
                        }
                    }
                ]
            },
            "proteins": [
                {
                    "accession": "p04637",
                    "protein_length": 393,
                    "source_database": "reviewed",
                    "organism": "9606",
                    "entry_protein_locations": [
                        {
                            "fragments": [
                                {
                                    "start": 3,
                                    "end": 366,
                                    "dc-status": "CONTINUOUS"
                                }
                            ],
                            "model": null,
                            "score": null
                        }
                    ]
                }
            ]
        },
        {
            "metadata": {
                "accession": "IPR008967",
                "name": "p53-like transcription factor, DNA-binding domain superfamily",
                "source_database": "interpro",
                "type": "homologous_superfamily",
                "integrated": null,
                "member_databases": {
                    "ssf": {
                        "SSF49417": "p53-like transcription factors"
                    }
                },
                "go_terms": [
                    {
                        "identifier": "GO:0003700",
                        "name": "DNA-binding transcription factor activity",
                        "category": {
                            "code": "F",
                            "name": "molecular_function"
                        }
                    },
                    {
                        "identifier": "GO:0006355",
                        "name": "regulation of DNA-templated transcription",
                        "category": {
                            "code": "P",
                            "name": "biological_process"
                        }
                    }
                ]
            },
            "proteins": [
                {
                    "accession": "p04637",
                    "protein_length": 393,
                    "source_database": "reviewed",
                    "organism": "9606",
                    "entry_protein_locations": [
                        {
                            "fragments": [
                                {
                                    "start": 97,
                                    "end": 287,
                                    "dc-status": "CONTINUOUS"
                                }
                            ],
                            "model": null,
                            "score": null
                        }
                    ]
                }
            ]
        },
        {
            "metadata": {
                "accession": "IPR010991",
                "name": "p53, tetramerisation domain",
                "source_database": "interpro",
                "type": "domain",
                "integrated": null,
                "member_databases": {
                    "pfam": {
                        "PF07710": "P53 tetramerisation motif"
                    }
                },
                "go_terms": [
                    {
                        "identifier": "GO:0051262",
                        "name": "protein tetramerization",
                        "category": {
                            "code": "P",
                            "name": "biological_process"
                        }
                    }
                ]
            },
            "proteins": [
                {
                    "accession": "p04637",
                    "protein_length": 393,
                    "source_database": "reviewed",
                    "organism": "9606",
                    "entry_protein_locations": [
                        {
                            "fragments": [
                                {
                                    "start": 319,
                                    "end": 357,
                                    "dc-status": "CONTINUOUS"
                                }
                            ],
                            "model": null,
                            "score": null
                        }
                    ]
                }
            ]
        },
        {
            "metadata": {
                "accession": "IPR011615",
                "name": "p53, DNA-binding domain",
                "source_database": "interpro",
                "type": "domain",
                "integrated": null,
                "member_databases": {
                    "cdd": {
                        "cd08367": "P53 DNA-binding domain"
                    },
                    "pfam": {
                        "PF00870": "P53 DNA-binding domain"
                    }
                },
                "go_terms": [
                    {
                        "identifier": "GO:0000976",
                        "name": "transcription cis-regulatory region binding",
                        "category": {
                            "code": "F",
                            "name": "molecular_function"
                        }
                    }
                ]
            },
            "proteins": [
                {
                    "accession": "p04637",
                    "protein_length": 393,
                    "source_database": "reviewed",
                    "organism": "9606",
                    "entry_protein_locations": [
                        {
                            "fragments": [
                                {
                                    "start": 100,
                                    "end": 288,
                                    "dc-status": "CONTINUOUS"
                                }
                            ],
                            "model": null,
                            "score": null
                        }
                    ]
                }
            ]
        },
        {
            "metadata": {
                "accession": "IPR012346",
                "name": "p53/RUNT-type transcription factor, DNA-binding domain superfamily",
                "source_database": "interpro",
                "type": "homologous_superfamily",
                "integrated": null,
                "member_databases": {
                    "cathgene3d": {
                        "G3DSA:2.60.40.720": "G3DSA:2.60.40.720"
                    }
                },
                "go_terms": [
                    {
                        "identifier": "GO:0003677",
                        "name": "DNA binding",
                        "category": {
                            "code": "F",
                            "name": "molecular_function"
                        }
                    },
                    {
                        "identifier": "GO:0003700",
                        "name": "DNA-binding transcription factor activity",
                        "category": {
                            "code": "F",
                            "name": "molecular_function"
                        }
                    },
                    {
                        "identifier": "GO:0006355",
                        "name": "regulation of DNA-templated transcription",
                        "category": {
                            "code": "P",
                            "name": "biological_process"
                        }
                    },
                    {
                        "identifier": "GO:0005634",
                        "name": "nucleus",
                        "category": {
                            "code": "C",
                            "name": "cellular_component"
                        }
                    }
                ]
            },
            "proteins": [
                {
                    "accession": "p04637",
                    "protein_length": 393,
                    "source_database": "reviewed",
                    "organism": "9606",
                    "entry_protein_locations": [
                        {
                            "fragments": [
                                {
                                    "start": 95,
                                    "end": 294,
                                    "dc-status": "CONTINUOUS"
                                }
                            ],
                            "model": null,
                            "score": null
                        }
                    ]
                }
            ]
        },
        {
            "metadata": {
                "accession": "IPR013872",
                "name": "p53 transactivation domain",
                "source_database": "interpro",
                "type": "domain",
                "integrated": null,
                "member_databases": {
                    "pfam": {
                        "PF08563": "P53 transactivation motif"
                    }
                },
                "go_terms": [
                    {
                        "identifier": "GO:0005515",
                        "name": "protein binding",
                        "category": {
                            "code": "F",
                            "name": "molecular_function"
                        }
                    }
                ]
            },
            "proteins": [
                {
                    "accession": "p04637",
                    "protein_length": 393,
                    "source_database": "reviewed",
                    "organism": "9606",
                    "entry_protein_locations": [
                        {
                            "fragments": [
                                {
                                    "start": 6,
                                    "end": 30,
                                    "dc-status": "CONTINUOUS"
                                }
                            ],
                            "model": null,
                            "score": null
                        }
                    ]
                }
            ]
        },
        {
            "metadata": {
                "accession": "IPR036674",
                "name": "p53-like tetramerisation domain superfamily",
                "source_database": "interpro",
                "type": "homologous_superfamily",
                "integrated": null,
                "member_databases": {
                    "cathgene3d": {
                        "G3DSA:4.10.170.10": "p53-like tetramerisation domain"
                    },
                    "ssf": {
                        "SSF47719": "p53 tetramerization domain"
                    }
                },
                "go_terms": [
                    {
                        "identifier": "GO:0051262",
                        "name": "protein tetramerization",
                        "category": {
                            "code": "P",
                            "name": "biological_process"
                        }
                    }
                ]
            },
            "proteins": [
                {
                    "accession": "p04637",
                    "protein_length": 393,
                    "source_database": "reviewed",
                    "organism": "9606",
                    "entry_protein_locations": [
                        {
                            "fragments": [
                                {
                                    "start": 319,
                                    "end": 360,
                                    "dc-status": "CONTINUOUS"
                                }
                            ],
                            "model": null,
                            "score": null
                        }
                    ]
                }
            ]
        },
        {
            "metadata": {
                "accession": "IPR040926",
                "name": "Cellular tumor antigen p53, transactivation domain 2",
                "source_database": "interpro",
                "type": "domain",
                "integrated": null,
                "member_databases": {
                    "pfam": {
                        "PF18521": "Transactivation domain 2"
                    }
                },
                "go_terms": null
            },
            "proteins": [
                {
                    "accession": "p04637",
                    "protein_length": 393,
                    "source_database": "reviewed",
                    "organism": "9606",
                    "entry_protein_locations": [
                        {
                            "fragments": [
                                {
                                    "start": 35,
                                    "end": 59,
                                    "dc-status": "CONTINUOUS"
                                }
                            ],
                            "model": null,
                            "score": null
                        }
                    ]
                }
            ]
        }
    ]
}'''