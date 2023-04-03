@echo off
rem input example: "D:\Education Zone\Programming world\Assembly\PostBuildCmd.bat" "D:\Education Zone\Programming world\Learning\MyLearning\WPF\Infragistics\InfragisticsApp\bin" "D:\Education Zone\Programming world\Learning\MyLearning\WPF\Infragistics\InfragisticsApp\..\..\..\..\..\Assembly\Executable\InfragisticsApp"
set source=%1
set target=%2

IF EXIST %source% (
	rem echo.
	rem echo.
	rem echo Copying %source% to %target%
	rem echo.
	rem echo.
	rem xcopy /Y /I /S %source% %target%

	rem del /q %source%*
	rem for /d %%x in (%source%*) do @rd /s /q "%%x"

	IF EXIST %target% (
		echo.
		echo.
		echo Deleting %target%
		echo.
		echo.
		del /q %target%*
		for /d %%x in (%target%*) do @rd /s /q "%%x"
	)
	
	echo.
	echo.
	echo Moving %source% to %target%
	echo.
	echo.
	move /Y %source% %target%
	
) ELSE (
	echo.
	echo.
	echo Source NOT found %source% 
	echo.
	echo.
)