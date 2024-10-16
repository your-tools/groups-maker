from argparse import ArgumentParser
from pathlib import Path

from teams_maker.teams import create_teams, get_team_name, check_name_provider


def main() -> None:
    parser = ArgumentParser(prog="teams-maker")
    parser.add_argument("partipant_list", type=Path)
    parser.add_argument("--team-size", type=int, required=True)
    parser.add_argument("--name-provider")
    parser.add_argument("--offset", type=int, default=0)
    args = parser.parse_args()

    list_path = args.partipant_list
    team_size = args.team_size
    name_provider = args.name_provider
    offset = args.offset
    participants = list_path.read_text().splitlines()

    teams = create_teams(participants, team_size)
    check_name_provider(name_provider, num_teams=len(teams))
    for index, team in enumerate(teams):
        team_name = get_team_name(
            name_provider=name_provider, index=index, offset=offset
        )
        print("-" * 10, "Team", team_name, "-" * 10)
        for partipant in sorted(team):
            print(partipant)
        print()


if __name__ == "__main__":
    main()
