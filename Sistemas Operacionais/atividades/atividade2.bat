@echo off
chcp 65001 >nul
::LoopRede
ipconfig

set /p inf="testar conectividade, digite a informação: "

ping %inf% 
set /p opcao="deseja continuar ? (S/N)"
if "%opcao%"=="s" (
	goto LoopRede
	)
