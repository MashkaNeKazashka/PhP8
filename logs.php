<?php
class Logger {
    private $logFile;

    public function __construct($file) {
        $this->logFile = $file;
    }

    public function log($message) {
        $timestamp = date("Y-m-d H:i:s");
        $logMessage = "[$timestamp] $message\n";
        file_put_contents($this->logFile, $logMessage, FILE_APPEND);
    }

    public function readLogs() {
        if (!file_exists($this->logFile)) {
            return "Логи отсутствуют.";
        }
        return file_get_contents($this->logFile);
    }
}

$logger = new Logger("app.log");
$logger->log("Пользователь вошел в систему");
$logger->log("Пользователь выполнил действие");
echo $logger->readLogs();
?>
