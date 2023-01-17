
haz = Hazard.from_mat(HAZ_DEMO_MAT)  # Set hazard
haz.check()
ent = Entity.from_excel(ENT_TEMPLATE_XLS)  # Set exposures
ent.check()
imp = Impact()
imp.calc(ent.exposures, ent.impact_funcs, haz)
imp.calc_freq_curve().plot()