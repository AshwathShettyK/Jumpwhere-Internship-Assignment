-- Drop and recreate cleanly
DROP DATABASE IF EXISTS nhl_db;
CREATE DATABASE nhl_db;
USE nhl_db;

-- TEAM table
CREATE TABLE IF NOT EXISTS Team (
    team_id     INT          NOT NULL AUTO_INCREMENT,
    name        VARCHAR(100) NOT NULL,
    city        VARCHAR(100) NOT NULL,
    coach       VARCHAR(100) NOT NULL,
    captain_id  INT          NULL,
    PRIMARY KEY (team_id)
);

-- PLAYER table
CREATE TABLE IF NOT EXISTS Player (
    player_id   INT          NOT NULL AUTO_INCREMENT,
    name        VARCHAR(100) NOT NULL,
    position    VARCHAR(50)  NOT NULL,
    skill_level INT          NOT NULL,
    team_id     INT          NOT NULL,
    PRIMARY KEY (player_id),
    CONSTRAINT fk_player_team
        FOREIGN KEY (team_id) REFERENCES Team(team_id)
        ON DELETE RESTRICT ON UPDATE CASCADE
);

-- Add captain FK back to Team
ALTER TABLE Team
    ADD CONSTRAINT fk_team_captain
        FOREIGN KEY (captain_id) REFERENCES Player(player_id)
        ON DELETE SET NULL ON UPDATE CASCADE;

-- INJURY_RECORD weak entity
CREATE TABLE IF NOT EXISTS Injury_Record (
    injury_id   INT          NOT NULL AUTO_INCREMENT,
    player_id   INT          NOT NULL,
    inj_date    DATE         NOT NULL,
    description VARCHAR(255) NOT NULL,
    PRIMARY KEY (injury_id),
    CONSTRAINT fk_injury_player
        FOREIGN KEY (player_id) REFERENCES Player(player_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

-- GAME table (removed multi-column CHECK constraint)
CREATE TABLE IF NOT EXISTS Game (
    game_id        INT  NOT NULL AUTO_INCREMENT,
    game_date      DATE NOT NULL,
    host_team_id   INT  NOT NULL,
    guest_team_id  INT  NOT NULL,
    host_score     INT  NOT NULL DEFAULT 0,
    guest_score    INT  NOT NULL DEFAULT 0,
    PRIMARY KEY (game_id),
    CONSTRAINT fk_game_host
        FOREIGN KEY (host_team_id)  REFERENCES Team(team_id)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_game_guest
        FOREIGN KEY (guest_team_id) REFERENCES Team(team_id)
        ON DELETE RESTRICT ON UPDATE CASCADE
);