from mako.lookup import TemplateLookup


tpl_lookup = TemplateLookup(directories=['templates/desktop'],
                            output_encoding='utf-8', encoding_errors='replace')
