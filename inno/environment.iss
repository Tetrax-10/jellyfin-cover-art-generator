const
  EnvironmentKey = 'SYSTEM\CurrentControlSet\Control\Session Manager\Environment';
  WM_SETTINGCHANGE = $001A;
  SMTO_ABORTIFHUNG = $0002;
  
type
  WPARAM = LongWord;
  LPARAM = LongInt;
  LRESULT = LongInt;
  PChar = String;
  
function SendMessageTimeout(hWnd: HWND; Msg: UINT; wParam: WPARAM; lParam: PChar;
  fuFlags, uTimeout: UINT; out lpdwResult: DWORD): LRESULT;
  external 'SendMessageTimeoutW@user32.dll stdcall';

function PosEx(const SubStr, S: String; Offset: Integer): Integer;
var
  i: Integer;
begin
  for i := Offset to Length(S) - Length(SubStr) + 1 do
  begin
    if Copy(S, i, Length(SubStr)) = SubStr then
    begin
      Result := i;
      Exit;
    end;
  end;
  Result := 0;
end;  
  
function SplitString(const S: String; const Delimiter: String): TArrayOfString;
var
  PosStart, PosDel, Index: Integer;
begin
  SetArrayLength(Result, 0);
  PosStart := 1;
  Index := 0;

  repeat
    PosDel := PosEx(Delimiter, S, PosStart);
    if PosDel = 0 then
      PosDel := Length(S) + 1;

    SetArrayLength(Result, Index + 1);
    Result[Index] := Copy(S, PosStart, PosDel - PosStart);
    PosStart := PosDel + Length(Delimiter);
    Index := Index + 1;
  until PosStart > Length(S);
end;
   
procedure NotifyEnvironmentChange;
var
  ResultCode: DWORD;
begin
  SendMessageTimeout(HWND_BROADCAST, WM_SETTINGCHANGE, 0,
    PChar(ExpandConstant('Environment')), SMTO_ABORTIFHUNG, 5000, ResultCode);
end;

procedure EnvAddPath(Path: string);
var
  Paths: string;
  PathList: TArrayOfString;
  I: Integer;
  Found: Boolean;
begin
  if not RegQueryStringValue(HKEY_LOCAL_MACHINE, EnvironmentKey, 'Path', Paths) then
    Paths := '';

  PathList := SplitString(Paths, ';');
  Found := False;

  for I := 0 to GetArrayLength(PathList) - 1 do
  begin
    if CompareText(Trim(PathList[I]), Trim(Path)) = 0 then
    begin
      Found := True;
      break;
    end;
  end;

  if not Found then
  begin
    if (Length(Paths) > 0) and (Paths[Length(Paths)] <> ';') then
      Paths := Paths + ';';
    Paths := Paths + Path;

    if RegWriteStringValue(HKEY_LOCAL_MACHINE, EnvironmentKey, 'Path', Paths) then
    begin
      Log(Format('Added "%s" to PATH. New PATH: "%s"', [Path, Paths]));
      NotifyEnvironmentChange;
    end
    else
      Log(Format('Error adding "%s" to PATH. Original PATH: "%s"', [Path, Paths]));
  end;
end;

procedure EnvRemovePath(Path: string);
var
  Paths, CleanPaths: string;
  PathList: TArrayOfString;
  I: Integer;
begin
  if not RegQueryStringValue(HKEY_LOCAL_MACHINE, EnvironmentKey, 'Path', Paths) then
    exit;

  PathList := SplitString(Paths, ';');
  CleanPaths := '';

  for I := 0 to GetArrayLength(PathList) - 1 do
  begin
    if CompareText(Trim(PathList[I]), Trim(Path)) <> 0 then
    begin
      if CleanPaths <> '' then
        CleanPaths := CleanPaths + ';';
      CleanPaths := CleanPaths + PathList[I];
    end;
  end;

  if RegWriteStringValue(HKEY_LOCAL_MACHINE, EnvironmentKey, 'Path', CleanPaths) then
  begin
    Log(Format('Removed "%s" from PATH. New PATH: "%s"', [Path, CleanPaths]));
    NotifyEnvironmentChange;
  end
  else
    Log(Format('Error removing "%s" from PATH. Original PATH: "%s"', [Path, Paths]));
end;