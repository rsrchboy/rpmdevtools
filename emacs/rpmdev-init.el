(defvar rpmdev-packager-user-full-name nil)
(defvar rpmdev-packager-mail-address nil)

(defun rpmdev-init-packager ()
  "Initialize packager info."
  (let ((packager (shell-command-to-string "rpmdev-packager 2>/dev/null")))
    (cond
     ((string-match "\\(.*\\)\\s-+<\\([^>]+\\)>" packager)
      (setq rpmdev-packager-user-full-name (match-string 1 packager))
      (setq rpmdev-packager-mail-address (match-string 2 packager)))
     ((string-match "\\([^\\s<]+@[^\\s>]+\\)" packager)
      (setq rpmdev-packager-mail-address (match-string 1 packager)))
     ((string-match "^\\s-*\\(.*\\)\\s-*$" packager)
      (setq rpmdev-packager-user-full-name (match-string 1 packager))))))

(defun rpmdev-packager-mail-address ()
  "Get packager mail address."
  (if rpmdev-packager-mail-address
       rpmdev-packager-mail-address
    (rpmdev-init-packager)
    rpmdev-packager-mail-address))
    
(defun rpmdev-packager-user-full-name ()
  "Get packager full name."
  (if rpmdev-packager-user-full-name
       rpmdev-packager-user-full-name
    (rpmdev-init-packager)
    rpmdev-packager-user-full-name))

(defun rpmdev-new-rpm-spec-file-init ()
  (delete-region (point-min) (point-max))
  (set (make-local-variable 'buffer-file-coding-system) 'utf-8)
  (if buffer-file-name
      (call-process "rpmdev-newspec" nil t nil "-o" "-" buffer-file-name)
    (call-process "rpmdev-newspec" nil t nil "-o" "-"))
  (and indent-tabs-mode (tabify (point-min) (point-max)))
  (goto-char (point-min))
  (re-search-forward "^[A-Za-z]+:\\s-*$" nil t)
  (set-buffer-modified-p nil)
  (unless rpm-spec-user-mail-address
    (set (make-local-variable 'rpm-spec-user-mail-address)
         (rpmdev-packager-mail-address)))
  (unless rpm-spec-user-full-name
    (set (make-local-variable 'rpm-spec-user-full-name)
         (rpmdev-packager-user-full-name))))

(remove-hook 'rpm-spec-mode-new-file-hook 'rpm-spec-initialize)
(add-hook 'rpm-spec-mode-new-file-hook 'rpmdev-new-rpm-spec-file-init t)
