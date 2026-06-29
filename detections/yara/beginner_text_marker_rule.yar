rule Beginner_Text_Marker_Rule
{
    meta:
        author = "D0R07HY"
        description = "Beginner-friendly YARA rule that matches a simple educational text marker"
        purpose = "Learning YARA structure with a safe text-based example"

    strings:
        $marker1 = "FOR EDUCATIONAL PURPOSES ONLY"
        $marker2 = "Malware Analysis"
        $marker3 = "Cyber Security"

    condition:
        2 of ($marker*)
}
