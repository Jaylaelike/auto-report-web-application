import os
import os.path
import asyncio
import aiohttp
import ssl
import openpyxl
from io import BytesIO, IOBase


def upload_file_process():
    try:
            fileContent = './tempDir/data.xlsx'
            save_path = './'
            name_of_file = fileContent
            completeName = os.path.join(save_path, name_of_file)

            if (fileContent != ''):
                            url_list = ['https://script.google.com/macros/s/AKfycbwH4k8SD5F6duZLthsa2q3D2wtJvpcggY5HtMC479aB1yg91pchlGk65WVQaDVYfLhd_g/exec',
                                        'https://script.google.com/macros/s/AKfycbzx8ruu5KJiNctKp12OgFI3XP4dfn_ffDdRZMCD8mZmHbzKuYmfKzb7T8-cAz69mYdt-A/exec',
                                        'https://script.google.com/macros/s/AKfycbyoX7cM1Ejkeej7N-TKNAR--l6ZlGSBa0FPiy9jFHq0BU3xyMUbRyHoY5s5Wp9nM41ANg/exec',
                                        'https://script.google.com/macros/s/AKfycby2cC69FuKvS3-n1pG3WyE95Lj7CL9ut5k17BgYmbCCvjLB0GA8M5E5FU3K8ya8F_Xk/exec',
                                        'https://script.google.com/macros/s/AKfycbzsnI5ILJLerqWqLhKAPpgESAVDA8SNAnP3p2vMRT06SI-jD6GsP8bO4IB4_oeDRTs8Gw/exec',
                                        'https://script.google.com/macros/s/AKfycbzv9izLctRhphOIn4OD2HUgQQuttu8lOIfrh6Lod9W5mbtVVlyFQC1cwdP81SEtyH6oXQ/exec',
                                        'https://script.google.com/macros/s/AKfycbyWPDK5oe2RhlSxzDsDhVvooI_N90BmhIFdBengbgO7Aq6ZwAgvqhWdI1EyVfkGl9kW/exec',
                                        'https://script.google.com/macros/s/AKfycbyazX9wgJTKbF34n4z3QDM1fPLoRwtLho5RVWaHfg52gx-ewz4HgXzHzV9Bc-h9Fhcwew/exec',
                                        'https://script.google.com/macros/s/AKfycbywAXbCkS_7zTLEv2hUoPHs6aI9RCohwnX94kDb4j2fpomHbuqIUghsd6YImESsn7xdWA/exec',
                                        'https://script.google.com/macros/s/AKfycbwCn90h7bXc7L_L570Fx8k_GyEhSUrzo6eKBSrMn8lwYa42EcF1okSGBYiJrkwcZCT5QQ/exec',
                                        'https://script.google.com/macros/s/AKfycbyJi6htdI-uKUd5dsbMQrDO9VhDTuGEFWdLurhZONePg9_TcTHzSX9rCFKn65REIKRl-w/exec',
                                        'https://script.google.com/macros/s/AKfycbwJBTdWmfkZs8w3vstxTlvKgVvbfeQ-3PEEgFIrPvlIg9K12E_31BHi3wrVtHZfDbKDUg/exec',
                                        'https://script.google.com/macros/s/AKfycbzryrF3abgTU_9HllNohAJ9_4bSgkT6QRWasBrqQt0puNbJUGOhAI8xiOMzrUD1w2eN/exec',
                                        'https://script.google.com/macros/s/AKfycbxRFNFuoNBZj5M5xFX7o0mcraXPKSnGNI5DGHToNy9fAJPSU9_C-KqmdFPwtw1dJaQn/exec',
                                        'https://script.google.com/macros/s/AKfycbz2uX3RfbkDNguEoQN3K3aen1aM2t-GrUMEoJT-GvYqffSdVVJ0bwYm5uW5z1SHHFHaeQ/exec',
                                        'https://script.google.com/macros/s/AKfycbz3iuBRqvBcBnh3_imzbW0uefRUYwZM_TBPWYF_1zXo2FMAPYLQfm9mu6XcZbh6E7wp/exec',
                                        'https://script.google.com/macros/s/AKfycby-tNv2gLU-siv93gCtwU-Oc_HgQQ2UNXA3rhkH8zh-LI9BeyumnHYVp1-HR1VdjPgJ/exec',
                                        'https://script.google.com/macros/s/AKfycby3kmOHaBPIBt_t5XwN_SEtKjssXMvlu1UC89bOSGvt1Wl89ORInBgUeAEC1ohAQbMI/exec',
                                        'https://script.google.com/macros/s/AKfycbwTY9-Zj4_2JsL7dW2xlwD9Rne2eyfQmcB4ZFZ-Hn1NN4Z-Y9FYtaTGVsxgJfrvTaSq/exec',
                                        'https://script.google.com/macros/s/AKfycbyLksPAsU9lmw8XLASwFZWzLCAwk-g_N3z83Ixg1C-fqDUuSDmwCUpVdA2QcCsf4tQH/exec',
                                        'https://script.google.com/macros/s/AKfycbxqCIeBX7-1_tIl1EiIxDN0b_BW_nwi7jJeIlQybyWVi4tE8L1YVyLGqe258ff3gXjsOQ/exec',
                                        'https://script.google.com/macros/s/AKfycbwviJ3VJCyy0d1sRmOI0AfGasqkzVlEsRmoInCBwds5pvBStrJY3sE-K0JlN4TdQeg21g/exec'
                                    ]


            async def fetch(session, url):
                async with session.get(url, ssl=ssl.SSLContext()) as response:
                    return await response.json()


            async def fetch_all(urls, loop):
                async with aiohttp.ClientSession(loop=loop) as session:
                    results = await asyncio.gather(*[fetch(session, url) for url in urls], return_exceptions=True)
                    return results

            loop = asyncio.get_event_loop()
            urls = url_list
            htmls = loop.run_until_complete(fetch_all(urls, loop))
            #test = htmls[0]['MER']
            print(htmls)               


            #CHP                 
            ird_chp_lm_a = htmls[0]['IRD_A_LM']
            ird_chp_cn_a = htmls[0]['IRD_A_C/N']
            ird_chp_lm_b = htmls[0]['IRD_B_LM']
            ird_chp_cn_b = htmls[0]['IRD_B_C/N']
            ups_runtime_chp = htmls[0]['UPSRuntime']
            chp_upper = htmls[14]['upper']
            chp_lower = htmls[14]['lower']
            chp_fwupper = htmls[14]['FWD_lower']
            chp_fwlower = htmls[14]['FWD_upper']
            chp_load_ups = htmls[21]['loadCHP']
            sfn_chp_mux = htmls[20]['SFN_CHP_MUX']
            ems_chp_mux = htmls[20]['EMS_CHP_MUX']
            sfn_chp_res = htmls[20]['SFN_CHP_RES']
            ems_chp_res = htmls[20]['EMS_CHP_RES']

            #RNG
            ird_rng_lm_a = htmls[1]['IRD_A_LM']
            ird_rng_cn_a = htmls[1]['IRD_A_C/N']
            ird_rng_lm_b = htmls[1]['IRD_B_LM']
            ird_rng_cn_b = htmls[1]['IRD_B_C/N']
            #Convert minute to hours rng station
            ups_runtime_rng = htmls[1]['UPSRuntime']
            ups_runtime_rng_h = int(ups_runtime_rng / 60)
            ups_runtime_rng_min = int(ups_runtime_rng - 60)
            rng_upper = htmls[16]['upper']
            rng_lower = htmls[16]['lower']
            rng_fwupper = htmls[16]['FWD_upper']
            rng_fwlower = htmls[16]['FWD_lower']
            rng_load_ups = htmls[21]['loadRNG']
            sfn_rng_mux = htmls[20]['SFN_RNG_MUX']
            ems_rng_mux = htmls[20]['EMS_RNG_MUX']
            sfn_rng_res = htmls[20]['SFN_RNG_RES']
            ems_rng_res = htmls[20]['EMS_RNG_RES']

            #PKK
            ird_pkk_lm_a = htmls[2]['IRD_A_LM']
            ird_pkk_cn_a = htmls[2]['IRD_A_C/N']
            ird_pkk_lm_b = htmls[2]['IRD_B_LM']
            ird_pkk_cn_b = htmls[2]['IRD_B_C/N']
            ups_runtime_pkk = htmls[2]['UPSRuntime']
            pkk_load_ups = htmls[21]['loadPKK']
            sfn_pkk_mux = htmls[20]['SFN_PKK_MUX']
            ems_pkk_mux = htmls[20]['EMS_PKK_MUX']
            sfn_pkk_res = htmls[20]['SFN_PKK_RES']
            ems_pkk_res = htmls[20]['EMS_PKK_RES']

            #HUA
            ird_hua_lm_a = htmls[3]['IRD_A_LM']
            ird_hua_cn_a = htmls[3]['IRD_A_C/N']
            ird_hua_lm_b = htmls[3]['IRD_B_LM']
            ird_hua_cn_b = htmls[3]['IRD_B_C/N']
            sfn_hua_mux = htmls[20]['SFN_HUA_MUX']
            ems_hua_mux = htmls[20]['EMS_HUA_MUX']
            sfn_hua_res = htmls[20]['SFN_HUA_RES']
            ems_hua_res = htmls[20]['EMS_HUA_RES']

            #PNP
            ird_pnp_lm = htmls[4]['IRD_A_LM']
            ird_pnp_cn = htmls[4]['IRD_A_CN']
            sfn_pnp = htmls[20]['SFN_PNP']
            em_pnp = htmls[20]['EMMIS_PNP']

            #PBI
            ird_pbi_lm_a = htmls[5]['IRD_A_LM']
            ird_pbi_cn_a = htmls[5]['IRD_A_CN']
            ird_pbi_lm_b = htmls[5]['IRD_B_LM']
            ird_pbi_cn_b = htmls[5]['IRD_B_CN']

            #TSK
            ird_tsk_lm_a = htmls[6]['IRD_A_LM']
            ird_tsk_lm_b = htmls[6]['IRD_B_LM']
            ird_tsk_cn_a = htmls[6]['IRD_A_CN']
            ird_tsk_cn_b = htmls[6]['IRD_B_CN']
            ups_runtime_tsk = htmls[6]['UPSRuntime']
            tsk_upper = htmls[15]['upper']
            tsk_lower = htmls[15]['lower']
            tsk_fwupper = htmls[15]['FWD_upper']
            tsk_fwlower = htmls[15]['FWD_lower']
            tsk_load_ups = htmls[21]['loadTSK']

            #LHS
            ird_lhs_lm_a = htmls[7]['IRD_A_LM']
            ird_lhs_lm_b = htmls[7]['IRD_B_LM']
            ird_lhs_cn_a = htmls[7]['IRD_A_CN']
            ird_lhs_cn_b = htmls[7]['IRD_B_CN']
            sfn_lhs = htmls[20]['SFN_LHS']
            em_lhs = htmls[20]['EMMIS_LHS']

            #SWI
            ird_swi_lm = htmls[8]['IRD_A_LM']
            ird_swi_cn = htmls[8]['IRD_A_CN']
            sfn_swi = htmls[20]['SFN_SWI']
            em_swi = htmls[20]['EMMIS_SWI']


            #KBR 
            ird_kbr_lm = htmls[9]['IRD_A_LM']
            ird_kbr_cn = htmls[9]['IRD_A_CN']
            sfn_kbr = htmls[20]['SFN_KBR']
            em_kbr = htmls[20]['EMMIS_KBR']


            #KPO
            ird_kpo_lm = htmls[10]['IRD_A_LM']
            ird_kpo_cn = htmls[10]['IRD_A_CN']
            ups_runtime_kpo = htmls[10]['UPS_Runtime']
            kpo_swrant = htmls[18]['SWR_ant']
            kpo_fwant = htmls[18]['FWD_ant']
            sfn_kpo = htmls[20]['SFN_KPO']
            em_kpo = htmls[20]['EMMIS_KPO']
            kpo_load_ups =htmls[21]['loadKPO']

            #PHT
            ird_pht_lm = htmls[11]['IRD_A_LM']
            ird_pht_cn = htmls[11]['IRD_A_CN'] 
            ups_runtime_pht = htmls[11]['UPS_Runtime']
            pht_swrant = htmls[17]['SWR_ant']
            pht_fwant = htmls[17]['FWD_ant'] 
            sfn_pht = htmls[20]['SFN_PHT']
            em_pht = htmls[20]['EMMIS_PHT']
            pht_load_ups = htmls[21]['loadPHT']

            #KAI KURABURI
            ird_kura_lm = htmls[12]['IRD_A_LM']
            ird_kura_cn = htmls[12]['IRD_A_CN']
            ups_runtime_kura = htmls[12]['UPS_Runtime']
            kai_swrant = htmls[19]['SWR_ant']
            kai_fwant = htmls[19]['FWD_ant']
            sfn_kai = htmls[20]['SFN_KAI'] 
            em_kai =  htmls[20]['EMMIS_KAI']
            kai_load_ups = htmls[21]['loadKAI']

            #TAS
            ird_tas_lm_a = htmls[13]['IRD_A_LM']
            ird_tas_cn_a = htmls[13]['IRD_A_CN']
            ird_tas_lm_b = htmls[13]['IRD_B_LM']
            ird_tas_cn_b = htmls[13]['IRD_B_CN']
            sfn_tas = htmls[20]['SFN_TAS']
            em_tas = htmls[20]['EMMIS_TAS']




            #Writer to workbook          
            wb = openpyxl.load_workbook(fileContent)

            #sheet = xfile.wb['Daily report']
            sheet = wb["CHP"]
            sheet["I6"] = ird_chp_lm_a
            sheet["J6"] = ird_chp_cn_a
            sheet["K6"] = ird_chp_lm_b
            sheet["L6"] = ird_chp_cn_b
            sheet["T6"] = ups_runtime_chp
            sheet["Q6"] = chp_upper
            sheet["O6"] = chp_lower
            sheet["P6"] = chp_fwupper
            sheet["N6"] = chp_fwlower
            sheet["R6"] = chp_load_ups

            

            sheet["I7"] = ird_rng_lm_a
            sheet["J7"] = ird_rng_cn_a
            sheet["K7"] = ird_rng_lm_b
            sheet["L7"] = ird_rng_cn_b
            sheet["S7"] = str(ups_runtime_rng_h)
            sheet["T7"] = str(ups_runtime_rng_min)
            sheet["Q7"] = rng_upper
            sheet["O7"] = rng_lower
            sheet["P7"] = rng_fwupper
            sheet["N7"] = rng_fwlower
            sheet["R7"] = rng_load_ups


            sheet["I12"] = ird_pkk_lm_a
            sheet["J12"] = ird_pkk_cn_a
            sheet["K12"] = ird_pkk_lm_b
            sheet["L12"] = ird_pkk_cn_b
            sheet["T12"] = ups_runtime_pkk
            sheet["R12"] = pkk_load_ups

            sheet["I13"] = ird_tas_lm_a
            sheet["J13"] = ird_tas_cn_a
            sheet["K13"] = ird_tas_lm_b
            sheet["L13"] = ird_tas_cn_b
            sheet["G13"] = sfn_tas
            sheet["H13"] = em_tas

            sheet["I14"] = ird_lhs_lm_a
            sheet["J14"] = ird_lhs_cn_a
            sheet["K14"] = ird_lhs_lm_b
            sheet["L14"] = ird_lhs_cn_b
            sheet["G14"] = sfn_lhs  
            sheet["H14"] = em_lhs    

            sheet["I8"] = ird_tsk_lm_a
            sheet["J8"] = ird_tsk_cn_a
            sheet["K8"] = ird_tsk_lm_b
            sheet["L8"] = ird_tsk_cn_b
            sheet["T8"] = ups_runtime_tsk
            sheet["Q8"] = tsk_upper
            sheet["O8"] = tsk_lower
            sheet["P8"] = tsk_fwupper
            sheet["N8"] = tsk_fwlower
            sheet["R8"] = tsk_load_ups

            sheet["I15"] = ird_pbi_lm_a
            sheet["J15"] = ird_pbi_cn_a
            sheet["K15"] = ird_pbi_lm_b
            sheet["L15"] = ird_pbi_cn_b

            sheet["I16"] = ird_hua_lm_a
            sheet["J16"] = ird_hua_cn_a
            sheet["K16"] = ird_hua_lm_b
            sheet["L16"] = ird_hua_cn_b

            sheet["I9"] = ird_pht_lm
            sheet["J9"] = ird_pht_cn
            sheet["T9"] = ups_runtime_pht
            sheet["O9"] = pht_swrant
            sheet["N9"] = pht_fwant
            sheet["E9"] = sfn_pht
            sheet["F9"] = em_pht
            sheet["R9"] = pht_load_ups


            sheet["I10"] = ird_kpo_lm
            sheet["J10"] = ird_kpo_cn
            sheet["T10"] = ups_runtime_kpo
            sheet["O10"] = kpo_swrant
            sheet["N10"] = kpo_fwant
            sheet["E10"] = sfn_kpo
            sheet["F10"] = em_kpo
            sheet["R10"] = kpo_load_ups
            

            sheet["I11"] = ird_kura_lm
            sheet["J11"] = ird_kura_cn
            sheet["T11"] = ups_runtime_kura
            sheet["O11"] = kai_swrant
            sheet["N11"] = kai_fwant
            sheet["E11"] = sfn_kai
            sheet["F11"] = em_kai
            sheet["R11"] = kai_load_ups

            sheet["I17"] = ird_swi_lm
            sheet["J17"] = ird_swi_cn
            sheet["E17"] = sfn_swi
            sheet["F17"] = em_swi

            sheet["I18"] = ird_pnp_lm
            sheet["J18"] = ird_pnp_cn
            sheet["E18"] = sfn_pnp
            sheet["F18"] = em_pnp

            sheet["I19"] = ird_kbr_lm
            sheet["J19"] = ird_kbr_cn
            sheet["E19"] = sfn_kbr
            sheet["F19"] = em_kbr

            # #NEC_SFN_EMSIION TIME
            sheet["E6"] = sfn_chp_mux
            sheet["F6"] = ems_chp_mux
            sheet["G6"] = sfn_chp_res
            sheet["H6"] = ems_chp_res
            sheet["E7"] = sfn_rng_mux
            sheet["F7"] = ems_rng_mux
            sheet["G7"] = sfn_rng_res
            sheet["H7"] = ems_rng_res
            sheet["E12"] = sfn_pkk_mux
            sheet["F12"] = ems_pkk_mux
            sheet["G12"] = sfn_pkk_res
            sheet["H12"] = ems_pkk_res
            sheet["E16"] = sfn_hua_mux
            sheet["F16"] = ems_hua_mux
            sheet["G16"] = sfn_hua_res
            sheet["H16"] = ems_hua_res


            wb.save('dataFinal.xlsx')
    except:
        pass   


upload_file_process()    