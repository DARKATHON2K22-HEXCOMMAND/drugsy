import drugsy

ds = drugsy.Drugsy()

drugs = ["Acamprosate","Actiq","Adderall","Alprazolam","Ambien","Amobarbital","Amphetamine","Amytal","Anexsia","Antabuse","Ativan","Avinza","Buprenorphine","Butalbital","Butorphanol","Campral","Carisoprodol","Chlordiazepoxide","Clonazepam","Clonidine","Cocaine","Codeine","Concerta","Crystal","Darvocet","Darvon","Demerol","Depade","Desoxyn","Dexedrine","Dextroamphetamine","Dextromethorphan","Di-Gesic","Diazepam","Dilaudid","Disulfiram","Duragesic","Duramorph","Ecstasy","Fentanyl","Fioricet","Fiorinal","Flunitrazepam","GHB","Halcion","Hash","Heroin","Hycodan","Hydrocodone","Hydromorphone","Kadian","Ketamine","Klonopin","LSD","Librium","Lorazepam","Lortab","Luminal","MSIR","Marijuana","Meperidine","Mescaline","Methadone","Methamphetamine","Methaqualone","Methylphenidate","Morphine","Mushrooms","Naltrexone","Nembutal","Norco","OxyContin","Oxycodone","PCP","Palladone","Pentobarbital","Percocet","Percodan","Peyote","Phenobarbital","Quaalude","Ritalin","Rohypnol","Roxicodone","Ryzolt","Secobarbital","Seconal","Soma","Speed","Steroids","Sublimaze","Suboxone","Subutex","Tramadol","Triazolam","Tussionex","Ultram","Valium","Vicodin","Vivitrol","Xanax","Xodol","Zolpidem"]

# for d in range(len(drugs)):
#     ds.scrape_torch(drugs[d])
#     ds.scrape_devil_search(drugs[d])
#     ds.scrape_onion_index(drugs[d])

ds.wait_for_tor()

for d in drugs:
    ds.scrape_torch(d)
    ds.scrape_devil_search(d)
    ds.scrape_onion_index(d)
