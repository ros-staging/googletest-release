@[for change_version, change_date, changelog, main_name, main_email in changelogs]@(Package) (@(change_version)@(DebianInc)@(Distribution)) --endhook /tmp/test.sh); urgency=high

@(changelog)

 -- @(main_name) <@(main_email)>  @(change_date)

@[end for]
